from django.urls import path
from . import views

app_name = 'medical_cooperative'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('inspections/', views.inspections, name='inspections'),
    path('medicines/', views.medicines, name='medicines')
]
