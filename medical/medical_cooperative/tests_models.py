from django.test import TestCase
from medical_cooperative.models import Inspections, db_medicines, Doctors


class InspectionsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Inspections.objects.create(date="2022-12-03", patient_name=('Имя'), gender=('м'), date_of_birth="2000-10-01", address=('Мск'), diagnosis=('diagnosis'), appointment=('appointment'), doctor=('doctor'))


class db_medicinesModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        db_medicines.objects.create(name=('Имя'), instructions=('instructions'), intended_action=('intended_action'), side_effects=('side_effects'), disease=('disease'))

    def test_name_label(self):
        db_medicine = db_medicines.objects.get(id=1)
        field_label = db_medicine._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_disease_label(self):
        db_medicine = db_medicines.objects.get(id=1)
        field_label = db_medicine._meta.get_field('disease').verbose_name
        self.assertEquals(field_label, 'disease')

    def test_instructions_max_length(self):
        db_medicine = db_medicines.objects.get(id=1)
        max_length = db_medicine._meta.get_field('instructions').max_length
        self.assertEquals(max_length, 1000)

    def test_side_effects_max_length(self):
        db_medicine = db_medicines.objects.get(id=1)
        max_length = db_medicine._meta.get_field('side_effects').max_length
        self.assertEquals(max_length, 500)


class DoctorsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Doctors.objects.create(name=('Имя'), specialization=('specialization'))

    def test_name_label(self):
        doctor = Doctors.objects.get(id=1)
        field_label = doctor._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_specialization_label(self):
        doctor = Doctors.objects.get(id=1)
        field_label = doctor._meta.get_field('specialization').verbose_name
        self.assertEquals(field_label, 'specialization')

    def test_name_max_length(self):
        doctor = Doctors.objects.get(id=1)
        max_length = doctor._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_specialization_max_length(self):
        doctor = Doctors.objects.get(id=1)
        max_length = doctor._meta.get_field('specialization').max_length
        self.assertEquals(max_length, 50)