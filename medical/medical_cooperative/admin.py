from django.contrib import admin
from medical_cooperative.models import Inspections
from medical_cooperative.models import db_medicines

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


class db_medicinesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('name', {'fields': ['name']}),
        ('instructions', {'fields': ['instructions']}),
        ('intended_action', {'fields': ['intended_action']}),
        ('side_effects', {'fields': ['side_effects']})
    ]


admin.site.register(Inspections, InspectionsAdmin)
admin.site.register(db_medicines, db_medicinesAdmin)
