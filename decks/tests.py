from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from decks.models import Deck


class DeckTests(APITestCase):
    def setUp(self):
        user = User.objects.create_user('test user')

        self.client.force_login(user=user)
    #     Animal.objects.create(name="lion", sound="roar")
    #     Animal.objects.create(name="cat", sound="meow")

    def test_create_deck(self):
        # url = reverse('decks')
        data = {'name': 'New Deck'}
        response = self.client.post('/decks/', data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Deck.objects.count(), 1)
        self.assertEqual(Deck.objects.get().name, 'New Deck')