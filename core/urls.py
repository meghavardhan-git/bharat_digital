from django.urls import path
from . import views

urlpatterns = [
    path('mgnrega/', views.mgnrega_dashboard, name='mgnrega_dashboard'),
]
