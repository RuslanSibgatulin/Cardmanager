from django.forms import DateTimeInput, ModelForm, NumberInput, Select

from .models import Card, Purchase


class CardStatusForm(ModelForm):
    class Meta:
        model = Card
        fields = ["status"]
        widgets = {
            "status": Select(
                attrs={"class": "form-select"}
            ),
        }


class PurchaseByCardForm(ModelForm):
    class Meta:
        model = Purchase
        fields = ["amount", "buytime"]
        widgets = {
            "buytime": DateTimeInput(
                attrs={"class": "form-control"}
            ),
            "amount": NumberInput(
                attrs={"class": "form-control", "step": "0.01"}
            ),
        }
