from django.core.management.base import BaseCommand
from core.models import DistrictData
import requests
from decouple import config

API_KEY = config('MGNREGA_API_KEY')

class Command(BaseCommand):
    help = "Fetches MGNREGA district-level data from data.gov.in and saves it"

    def handle(self, *args, **options):
        url = "https://api.data.gov.in/resource/ee03643a-ee4c-48c2-ac30-9f2ff26ab722"
        params = {
            "api-key": API_KEY,
            "format": "json",
            "limit": 100,
            "filters[state_name]": "TAMIL NADU"
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            records = data.get("records", [])
            if not records:
                self.stdout.write(self.style.WARNING("No records found"))
                return

            DistrictData.objects.all().delete()  # optional — clears old data

            objs = []
            for rec in records:
                objs.append(DistrictData(
                    fin_year=rec.get("fin_year"),
                    month=rec.get("month"),
                    state=rec.get("state_name"),
                    district=rec.get("district_name"),
                    approved_labour_budget=rec.get("Approved_Labour_Budget"),
                    avg_wage_rate=rec.get("Average_Wage_rate_per_day_per_person"),
                    avg_days_employment=rec.get("Average_days_of_employment_provided_per_Household"),
                    differently_abled=rec.get("Differently_abled_persons_worked"),
                    wages=rec.get("Wages"),
                    women_persondays=rec.get("Women_Persondays"),
                    total_individuals_worked=rec.get("Total_Individuals_Worked"),
                ))

            DistrictData.objects.bulk_create(objs)
            self.stdout.write(self.style.SUCCESS(f"{len(objs)} records fetched and saved successfully!"))

        except requests.exceptions.RequestException as e:
            self.stderr.write(self.style.ERROR(f"Error fetching data: {e}"))
