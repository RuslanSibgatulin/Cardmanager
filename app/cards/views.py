from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import HttpRequest, HttpResponseRedirect
from django.views.generic import ListView, UpdateView, View
from django.views.generic.edit import FormView

from .forms import CardGeneratorForm, CardStatusForm, PurchaseByCardForm
from .models import Card, Purchase


class CardListView(ListView):
    template_name = "cards_list.html"
    model = Card
    paginate_by = 12

    def get_queryset(self):
        if self.request.GET.get("q", ""):
            query = self.request.GET.get("q")
            queryset = Card.objects.filter(
                Q(number__contains=query) | Q(series__contains=query) | Q(
                    release_at__contains=query) | Q(expiration_at__contains=query) | Q(status__icontains=query)
            )
        else:
            queryset = Card.objects.all()

        return queryset


class CardUpdateView(SuccessMessageMixin, UpdateView):
    template_name = "cards/card_detail.html"
    model = Card
    form_class = CardStatusForm
    success_url = "#"
    success_message = "Card updated successfully."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["purchase_list"] = Purchase.objects.filter(card=self.object.pk).order_by("-buytime")
        return context


class PurchaseCreateView(View):
    http_method_names = ["post"]
    model = Purchase

    def post(self, request: HttpRequest, *args, **kwargs):
        form = PurchaseByCardForm(request.POST)
        if form.is_valid():
            form.save()

        for err in form.errors.as_data().values():
            err_msg = [_.message for _ in err]
            for msg in err_msg:
                messages.error(request, msg)

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class CardGeneratorView(FormView):
    form_class = CardGeneratorForm
    template_name = "cards/card_gen.html"
    success_url = "#"

    def post(self, request: HttpRequest, *args, **kwargs):
        form = CardGeneratorForm(request.POST)

        if form.is_valid():
            series = int(form.cleaned_data["series"])
            expiration = int(form.cleaned_data["expiration"])
            count = int(form.cleaned_data["count"])
            last_card_in_series = Card.objects.filter(number__startswith=series).order_by("-number").first()
            start_num = 1
            if last_card_in_series:
                start_num = int(last_card_in_series.number[8:]) + 1

            if start_num + count < 99999999:
                for i in range(count):
                    Card.objects.create(
                        series=series,
                        number="{}{:08d}".format(series, start_num + i),
                        expiration_at=datetime.now() + relativedelta(months=expiration)
                    )
                messages.info(request, f"Cards series {series} created. Numbers [{start_num}-{start_num+count-1}]")
            else:
                messages.error(request, f"Not enough available numbers in series {series}")

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
