from django.shortcuts import render
from .models import DistrictData as MGNREGADashboard    

def mgnrega_dashboard(request):
    data = MGNREGADashboard.objects.all()

    district = request.GET.get('district')
    year = request.GET.get('year')

    if district:
        data = data.filter(district=district)
    if year:
        data = data.filter(fin_year=year)

    # calculate wages in lakhs
    for item in data:
        item.wages_lakhs = float(item.wages) / 100000

    districts = MGNREGADashboard.objects.values_list('district', flat=True).distinct()
    years = MGNREGADashboard.objects.values_list('fin_year', flat=True).distinct()

    return render(request, 'mgnrega_dashboard.html', {
        'data': data,
        'districts': districts,
        'years': years,
        'selected_district': district,
        'selected_year': year
    })

