from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cards/', include('cards.urls', namespace="cards")),
]
