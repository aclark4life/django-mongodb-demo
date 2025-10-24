from django.contrib import admin
from .models import Patient
from django_mongodb_backend.admin import EncryptedModelAdmin


@admin.register(Patient)
class PatientAdmin(EncryptedModelAdmin):
    pass
