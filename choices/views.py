from django.db.models import Count
from rest_framework import serializers, generics, permissions, viewsets

from cards.models import Card
from cards.serializers import CardSerializer
from choices.models import Choice


class ChoiceSerializer(serializers.ModelSerializer):
    card = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Card.objects)
    card_id = serializers.IntegerField(source='card__id', read_only=True)
    card_name = serializers.CharField(source='card__name', read_only=True)
    card_content = serializers.CharField(source='card__content', read_only=True)
    total_choices = serializers.IntegerField(read_only=True)

    class Meta:
        model = Choice
        fields = ['card', 'card_id', 'card_name', 'card_content', 'total_choices']


class ChoicesViewSet(generics.ListCreateAPIView, viewsets.GenericViewSet):
    queryset = Choice.objects.values('card__name', 'card__content', 'card__id').annotate(total_choices=Count('id'))
    serializer_class = ChoiceSerializer
    permission_classes = [permissions.AllowAny]
