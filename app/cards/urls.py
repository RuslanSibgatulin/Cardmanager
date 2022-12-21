from django.urls import path

from .views import CardListView, CardUpdateView

app_name = "cards"

urlpatterns = [
    path('', CardListView.as_view(), name='card-list'),
    path('<int:pk>', CardUpdateView.as_view(), name='card-detail')
]
