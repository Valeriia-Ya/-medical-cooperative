from django.shortcuts import render
from .models import Inspections


# Create your views here.
def home(request):
    return render(request, 'home.html')


def inspections(request):
    info = Inspections.objects.all()
    return render(request, 'inspections.html', {'info': info})
