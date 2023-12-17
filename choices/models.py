from django.db import models

from cards.models import Card


class Choice(models.Model):
    selected_card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='+')
    other_card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='+')
    created_at = models.DateTimeField()
