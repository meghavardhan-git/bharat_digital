# core/models.py
from django.db import models

class DistrictData(models.Model):
    fin_year = models.CharField(max_length=20, default="2024-2025")
    month = models.CharField(max_length=10)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    approved_labour_budget = models.BigIntegerField(null=True, blank=True)
    avg_wage_rate = models.FloatField(null=True, blank=True)
    avg_days_employment = models.FloatField(null=True, blank=True)
    differently_abled = models.IntegerField(null=True, blank=True)
    wages = models.FloatField(null=True, blank=True)
    women_persondays = models.FloatField(null=True, blank=True)
    total_individuals_worked = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.district}, {self.state} - {self.fin_year} {self.month}"
