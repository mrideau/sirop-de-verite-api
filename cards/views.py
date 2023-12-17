from rest_framework import viewsets

from cards.models import Card
from cards.serializers import CardSerializer
from utils.permissions import IsAdminOrReadOnly


class CardViewSet(viewsets.ModelViewSet):
    lookup_field = 'slug'
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAdminOrReadOnly]