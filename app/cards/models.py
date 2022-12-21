from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


class CardState(models.TextChoices):
    NotActive = "NotActive"
    ACTIVE = "Active"
    EXPIRED = "Expired"


class Card(models.Model):
    series = models.IntegerField(
        _("card series"),
        blank=True,
        null=True
    )
    number = models.CharField(
        _("card number"),
        max_length=16,
        primary_key=True,
        validators=[RegexValidator(regex="\\d{16}")]
    )
    release_at = models.DateField(
        _("release date"),
        auto_now_add=True,
        editable=False
    )
    expiration_at = models.DateField(_("expiration date"))
    used_at = models.DateTimeField(
        _("used date"),
        null=True,
        blank=True,
        editable=False
    )
    status = models.CharField(
        _("status"),
        max_length=50,
        choices=CardState.choices,
        default=CardState.NotActive
    )
    amount = models.FloatField(_("ammount"), editable=False, default=0)


class Purchase(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    amount = models.FloatField(_("ammount"), default=0)
    buytime = models.DateTimeField(
        _("time"),
        # auto_now_add=True
    )
