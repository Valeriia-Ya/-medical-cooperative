from django.shortcuts import render
<<<<<<< HEAD
=======
from .models import Inspections, db_medicines, Doctors
>>>>>>> main


# Create your views here.
def home(request):
<<<<<<< HEAD
    return render(request, 'home.html')


def inspections(request):
    return render(request)
=======
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
>>>>>>> main
