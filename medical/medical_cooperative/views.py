from django.shortcuts import render
from .models import Inspections, db_medicines


# Create your views here.
def home(request):
    return render(request, 'home.html')


def inspections(request):
    info = Inspections.objects.all()
    return render(request, 'inspections.html', {'info': info})


def medicines(request):
    info = db_medicines.objects.all()
    return render(request, 'medicines.html', {'info': info})
