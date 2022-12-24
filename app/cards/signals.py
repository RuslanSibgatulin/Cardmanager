from typing import Any

from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from .models import Card, CardState


@receiver(pre_save, sender=Card)
def status_rule(sender: Any, instance: Card, **kwargs):
    if instance.status == CardState.EXPIRED:
        raise ValidationError(_("Card has expired. Any operations are prohibited."))
