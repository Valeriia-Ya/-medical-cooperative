from django.shortcuts import render
from .models import Inspections, db_medicines, Doctors


# Create your views here.
def home(request):
    acc = Doctors.objects.get(pk=1)
    return render(request, 'home.html', {'acc': acc})


def inspections(request):
    acc = Doctors.objects.get(pk=1)
    info = Inspections.objects.all()
    return render(request, 'inspections.html', {'info': info, 'acc': acc})


def medicines(request):
    acc = Doctors.objects.get(pk=1)
    info = db_medicines.objects.all()
    return render(request, 'medicines.html', {'info': info, 'acc': acc})
