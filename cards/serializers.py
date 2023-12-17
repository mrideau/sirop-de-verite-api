from rest_framework import serializers

from cards.models import Card


class CardSerializer(serializers.ModelSerializer):
    flags = serializers.MultipleChoiceField(choices=Card.CardFlag)

    class Meta:
        model = Card
        fields = ['id', 'name', 'slug', 'deck', 'flags']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
            'deck': {'write_only': True}
        }
