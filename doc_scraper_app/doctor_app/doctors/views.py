from django.shortcuts import render
from .models import Doctor

def doctor_list(request):
    doctors = Doctor.objects.all()
    query = request.GET.get('search')
    if query:
        doctors = doctors.filter(name__icontains=query)
    return render(request, 'doctor_list.html', {'doctors': doctors})
