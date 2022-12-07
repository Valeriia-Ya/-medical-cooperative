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
    if request.POST:
        name = request.POST['inputName']
        instructions = request.POST['inputInstructions']
        intended_action = request.POST['inputIntended_action']
        side_effects = request.POST['inputSide_effects']
        db_medicines.objects.create(name=name, instructions=instructions, intended_action=intended_action, side_effects=side_effects)
    return render(request, 'medicines.html', {'info': info, 'acc': acc})


def statistics_1(request):
    acc = Doctors.objects.get(pk=1)
    doctors = Doctors.objects.all()
    if request.POST:
        name_doc = request.POST['inputDoctor']
        inputDate = request.POST['inputDate']
        if name_doc == "Все":
            result = Inspections.objects.filter(date=inputDate).count()
        else:
            result = Inspections.objects.filter(doctor=name_doc, date=inputDate).count()
        info = {'name': name_doc, 'date': inputDate, 'result': result}
        return render(request, 'statistics_1.html', {'acc': acc, 'doctors': doctors, 'info': info})
    return render(request, 'statistics_1.html', {'acc': acc, 'doctors': doctors})


def statistics_2(request):
    acc = Doctors.objects.get(pk=1)
    diseases = Inspections.objects.values('diagnosis').distinct()
    if request.POST:
        disease = request.POST['inputDisease']
        result = Inspections.objects.filter(diagnosis=disease).count()
        info = {'disease': disease, 'result': result}
        return render(request, 'statistics_2.html', {'acc': acc, 'info': info, 'diseases': diseases})
    return render(request, 'statistics_2.html', {'acc': acc, 'diseases': diseases})
