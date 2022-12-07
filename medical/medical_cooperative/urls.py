from django.urls import path
from . import views

app_name = 'medical_cooperative'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('inspections/', views.inspections, name='inspections'),
    path('medicines/', views.medicines, name='medicines'),
    path('statistics_1/', views.statistics_1, name='statistics_1'),
    path('statistics_2/', views.statistics_2, name='statistics_2')
]
