from django.shortcuts import render
from .models import Inspections, db_medicines, Doctors

pass = "pdct.1.1.20221127T184216Z.7b9c144b5992eb5c.be4a3e2356a92547a1ce82"

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
