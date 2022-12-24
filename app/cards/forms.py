from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Card, CardState, Purchase


class CardStatusForm(forms.ModelForm):

    status_choices = (
        (CardState.ACTIVE.value, CardState.ACTIVE.label),
        (CardState.BLOCKED.value, CardState.BLOCKED.label)
    )

    status = forms.ChoiceField(
        label=_("Status"),
        required=True,
        choices=status_choices,
        widget=forms.Select(
            attrs={"class": "form-select"}
        )
    )

    class Meta:
        model = Card
        fields = ["status"]


class PurchaseByCardForm(forms.ModelForm):
    # TODO: add fields
    class Meta:
        model = Purchase
        fields = ["card", "amount", "buytime"]
        widgets = {
            "buytime": forms.DateTimeInput(
                attrs={"class": "form-control"}
            ),
            "amount": forms.NumberInput(
                attrs={"class": "form-control", "step": "0.01"}
            ),
        }


class CardGeneratorForm(forms.Form):
    expiration_choices = (
        (1, _("1 month")),
        (6, _("6 months")),
        (12, _("1 year"))
    )

    series = forms.IntegerField(
        label=_("Series"),
        min_value=10000000,
        max_value=99999999,
        required=True,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "8 digits"}
        )
    )
    expiration = forms.ChoiceField(
        label=_("Expiration"),
        required=True,
        choices=expiration_choices,
        initial=(12, _("1 year")),
        widget=forms.Select(
            attrs={"class": "form-select"}
        )
    )
    count = forms.IntegerField(
        label=_("Count"),
        min_value=1,
        max_value=1000,
        required=True,
        widget=forms.NumberInput(
            attrs={"class": "form-control"}
        ),
    )
