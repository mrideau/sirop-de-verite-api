from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField

from decks.models import Deck


class Card(models.Model):
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='cards')
    no_alcohol = models.BooleanField(default=False)

    def __str__(self):
        return self.name
