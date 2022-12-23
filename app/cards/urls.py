from django.urls import path

from .views import CardListView, CardUpdateView, PurchaseCreateView

app_name = "cards"

urlpatterns = [
    path('', CardListView.as_view(), name='card-list'),
    path('<int:pk>', CardUpdateView.as_view(), name='card-detail'),
    path('<int:pk>/purchase/', PurchaseCreateView.as_view(), name='add-purchase')
]
