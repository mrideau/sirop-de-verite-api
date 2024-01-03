from django.db import models

from cards.models import Card


class Choice(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='choices')
    created_at = models.DateTimeField(auto_now_add=True)
