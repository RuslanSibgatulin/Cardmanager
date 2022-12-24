from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpRequest, HttpResponseRedirect
from django.views.generic import ListView, UpdateView, View

from .forms import CardStatusForm, PurchaseByCardForm
from .models import Card, Purchase


class CardListView(ListView):
    template_name = "cards_list.html"
    model = Card


class CardUpdateView(SuccessMessageMixin, UpdateView):
    template_name = "cards/card_detail.html"
    model = Card
    form_class = CardStatusForm
    success_url = "#"
    success_message = "Card updated successfully."

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

        for err in form.errors.as_data().values():
            err_msg = [_.message for _ in err]
            for msg in err_msg:
                messages.error(request, msg)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
