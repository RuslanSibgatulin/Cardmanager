from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, RegexValidator
from django.db import models
from django.db.models import F
from django.utils.translation import gettext_lazy as _


class CardState(models.TextChoices):
    NOTACTIVE = "NotActive", _("Not Active")
    ACTIVE = "Active", _("Active")
    BLOCKED = "Blocked", _("Blocked")
    EXPIRED = "Expired", _("Expired")


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
    status = models.CharField(
        _("status"),
        max_length=10,
        choices=CardState.choices,
        default=CardState.NOTACTIVE
    )
    amount = models.FloatField(_("ammount"), default=0)


class Purchase(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    amount = models.FloatField(_("ammount"), default=0, validators=[MinValueValidator(0.01)])
    buytime = models.DateTimeField(_("time"))

    def clean(self) -> None:
        if self.card.status != CardState.ACTIVE:
            raise ValidationError(_('Card is not active.'))

        if self.card.amount < self.amount:
            raise ValidationError(_('Insufficient funds.'))
        else:
            Card.objects.filter(pk=self.card.pk).update(amount=F('amount') - self.amount)

        return super().clean()
