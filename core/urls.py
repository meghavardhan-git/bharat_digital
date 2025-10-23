from django.urls import path
from . import views

urlpatterns = [
    path('', views.mgnrega_dashboard, name='mgnrega_dashboard'),  # root of this app
]
