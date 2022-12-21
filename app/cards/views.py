from django.views.generic import CreateView, ListView, UpdateView

from .forms import CardStatusForm
from .models import Card, Purchase


class CardListView(ListView):
    template_name = "cards_list.html"
    model = Card


class CardUpdateView(UpdateView):
    template_name = "cards/card_detail.html"
    model = Card
    form_class = CardStatusForm
    success_url = "#"


class PurchaseCreateView(CreateView):
    model = Purchase
