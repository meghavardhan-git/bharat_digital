from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mgnrega/', include('core.urls')),  # dashboard now at /mgnrega/
    path('', RedirectView.as_view(pattern_name='mgnrega_dashboard', permanent=False)),  # redirect root
]
