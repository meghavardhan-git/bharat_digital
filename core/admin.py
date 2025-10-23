# core/admin.py
from django.contrib import admin
from .models import DistrictData

@admin.register(DistrictData)
class DistrictDataAdmin(admin.ModelAdmin):
    list_display = (
        "fin_year",
        "month",
        "state",
        "district",
        "approved_labour_budget",
        "avg_wage_rate",
        "avg_days_employment",
        "differently_abled",
        "wages",
        "women_persondays",
        "total_individuals_worked",
    )
    list_filter = ("state", "month", "fin_year")
    search_fields = ("state", "district")
