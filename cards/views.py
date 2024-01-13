import random

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from cards.models import Card
from cards.serializers import CardSerializer
from utils.permissions import IsAdminOrReadOnly


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAdminOrReadOnly]

    @action(detail=False, methods=['get'], url_path='randoms')
    def select_random_cards(self, request):
        decksStr = request.GET.get('decks')
        decks = decksStr.split(',') if decksStr else []
        no_alcohol = request.GET.get('noAlcohol', 'false')

        all_cards = Card.objects.all()

        if decks:
            all_cards = Card.objects.filter(deck_id__in=decks)

        if no_alcohol == 'true':
            all_cards = all_cards.filter(no_alcohol=True)

        shuffled_cards = list(all_cards)
        random.shuffle(shuffled_cards)
        selected_cards = shuffled_cards[:2]
        serializer = CardSerializer(selected_cards, many=True)

        return Response(serializer.data)