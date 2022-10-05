from django.contrib import admin
from medical_cooperative.models import Inspections

# Register your models here.
class InspectionsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('date', {'fields': ['date']}),
        ('patient_name', {'fields': ['patient_name']}),
        ('gender', {'fields': ['gender']}),
        ('date_of_birth', {'fields': ['date_of_birth']}),
        ('address', {'fields': ['address']}),
        ('diagnosis', {'fields': ['diagnosis']}),
        ('appointment', {'fields': ['appointment']}),
        ('doctor', {'fields': ['doctor']})
    ]


admin.site.register(Inspections, InspectionsAdmin)