from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from decks.models import Deck
from decks.serializers import DeckSerializer
from users.models import User


class DeckTests(APITestCase):
    def setUp(self):
        user = User.objects.create_superuser('Superuser', password='<PASSWORD>')
        self.client.force_login(user=user)

        Deck.objects.bulk_create([Deck(name="Deck 1"), Deck(name="Deck 2"), Deck(name="Deck 3")])

    def test_list_decks(self):
        response = self.client.get('/decks/')

        decks = Deck.objects.all()
        serializer = DeckSerializer(decks, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_deck(self):
        data = {'name': 'Deck 4'}
        response = self.client.post('/decks/', data)

        deck = Deck.objects.get(name=data['name'])
        serializer = DeckSerializer(deck)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, serializer.data)


    def test_update_deck(self):
        deck = Deck.objects.first()
        data = {'name': 'Renamed Deck'}
        response = self.client.put(f'/decks/{deck.id}/', data)

        deck = Deck.objects.get(name=data['name'])
        serializer = DeckSerializer(deck)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)