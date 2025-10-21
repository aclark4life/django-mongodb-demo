from django.contrib import admin  
from .models import Patient, PatientRecord, Billing  
  
  
@admin.register(Patient)  
class PatientAdmin(admin.ModelAdmin):  
    list_display = ("patient_name", "patient_id",)
    search_fields = ("patient_name", "patient_id")
    list_filter = ("patient_name",)
