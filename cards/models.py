from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField

from decks.models import Deck


class Card(models.Model):
    class CardFlag(models.TextChoices):
        ALCOHOL = "AL", _("Alcohol Related")

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    flags = MultiSelectField(choices=CardFlag.choices, blank=True, max_length=3)

    def __str__(self):
        return self.name
