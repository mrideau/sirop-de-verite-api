import rest_framework.permissions
from django.db import models
from django.db.models import Count
from rest_framework import serializers, generics, permissions, viewsets
from rest_framework.response import Response

from cards.models import Card
from cards.serializers import CardSerializer
from choices.models import Choice


class ChoicesSerializer(serializers.ModelSerializer):
    # selected_card = CardSerializer(read_only=True)
    # selected_card = serializers.SerializerMethodField()
    count = serializers.IntegerField(read_only=True)
    # other_card = CardSerializer()

    class Meta:
        model = Choice
        fields = ['count']


class ChoicesViewSet(generics.ListCreateAPIView, viewsets.GenericViewSet):
    queryset = Choice.objects.values('selected_card').annotate(count=Count('selected_card')).order_by('count')
    serializer_class = ChoicesSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
