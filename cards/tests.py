from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from cards.models import Card
from cards.serializers import CardSerializer
from decks.models import Deck
from users.models import User


class ListCardTest(APITestCase):
    def setUp(self):
        deck = Deck.objects.create(name='Deck 1')
        Card.objects.bulk_create([Card(name="Card 1", content="Card content", deck=deck),
                                  Card(name="Card 2", content="Card content", deck=deck),
                                  Card(name="Card 3", content="Card content", deck=deck)])

    def test_list_cards(self):
        response = self.client.get('/cards/')

        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


class CreateCardTest(APITestCase):
    def setUp(self):
        user = User.objects.create_superuser('Superuser', password='<PASSWORD>')
        self.client.force_login(user=user)

        self.deck = Deck.objects.create(name='Deck 1')

    def test_create_card(self):
        url = reverse('card-list')
        data = {'name': 'Card 4', 'content': 'Card content', 'deck': self.deck.id}
        response = self.client.post(url, data)

        card = Card.objects.last()
        serializer = CardSerializer(card)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, serializer.data)


class UpdateCardTest(APITestCase):
    def setUp(self):
        user = User.objects.create_superuser('Superuser', password='<PASSWORD>')
        self.client.force_login(user=user)

        deck = Deck.objects.create(name='Deck 1')
        self.card = Card.objects.create(name="Card 1", content="Card content", deck=deck)

    def test_update_card(self):
        url = reverse('card-detail', kwargs={'pk': self.card.pk})

        updated_data = {
            'name': 'Renamed card',
            'content': 'New content',
            'deck': self.card.deck.id
        }

        response = self.client.put(url, updated_data)

        card = Card.objects.get(name=updated_data['name'])
        serializer = CardSerializer(card)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
