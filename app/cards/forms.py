from django.forms import DateTimeInput, ModelForm, NumberInput, Select
from django.utils.translation import gettext_lazy as _

from .models import Card, CardState, Purchase


class CardStatusForm(ModelForm):

    status_choices = (
        (CardState.ACTIVE.value, CardState.ACTIVE.label),
        (CardState.BLOCKED.value, CardState.BLOCKED.label)
    )

    class Meta:
        model = Card
        fields = ["status"]
        widgets = {
            "status": Select(
                attrs={"class": "form-select"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["status"].choices = self.status_choices


class PurchaseByCardForm(ModelForm):
    class Meta:
        model = Purchase
        fields = ["card", "amount", "buytime"]
        widgets = {
            "buytime": DateTimeInput(
                attrs={"class": "form-control"}
            ),
            "amount": NumberInput(
                attrs={"class": "form-control", "step": "0.01"}
            ),
        }
