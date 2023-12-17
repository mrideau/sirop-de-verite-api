from rest_framework import viewsets

from decks.models import Deck
from decks.serializers import DeckSerializer
from utils.permissions import IsAdminOrReadOnly


class DeckViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    permission_classes = [IsAdminOrReadOnly]