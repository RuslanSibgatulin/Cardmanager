from django.core.exceptions import ValidationError
from django.http import (HttpRequest, HttpResponseBadRequest,
                         HttpResponseRedirect)
from django.views.generic import ListView, UpdateView, View

from .forms import CardStatusForm, PurchaseByCardForm
from .models import Card, CardState, Purchase


class CardListView(ListView):
    template_name = "cards_list.html"
    model = Card


class CardUpdateView(UpdateView):
    template_name = "cards/card_detail.html"
    model = Card
    form_class = CardStatusForm
    success_url = "#"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['purchase_list'] = Purchase.objects.filter(card=self.object.pk).order_by("-buytime")
        return context


class PurchaseCreateView(View):
    http_method_names = ['post']
    model = Purchase

    def post(self, request: HttpRequest, *args, **kwargs):
        form = PurchaseByCardForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        return HttpResponseBadRequest()
