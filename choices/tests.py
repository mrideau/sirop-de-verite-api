from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from cards.models import Card
from choices.models import Choice
from choices.views import ChoiceSerializer
from decks.models import Deck
from users.models import User


class CreateChoiceTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create_user('Superuser', password='<PASSWORD>')
        self.client.force_login(user=user)

        self.deck = Deck.objects.create(name='Deck 1')
        self.card = Card.objects.create(name='Card 1', content='Card content', deck=self.deck)

    def test_create_choice(self):
        url = reverse('choice-list')
        data = {'card': self.card.id}
        response = self.client.post(url, data)

        choice = Choice.objects.last()
        serializer = ChoiceSerializer(choice)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, serializer.data)
