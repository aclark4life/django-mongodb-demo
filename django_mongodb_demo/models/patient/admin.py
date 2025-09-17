from django.contrib import admin  
from .models import Patient, PatientRecord, Billing  
from djongo.admin import EmbeddedModelAdmin  
  
class BillingAdmin(EmbeddedModelAdmin):  
    model = Billing  
  
  
class PatientRecordAdmin(EmbeddedModelAdmin):  
    model = PatientRecord  
    inlines = [BillingAdmin]  
  
  
@admin.register(Patient)  
class PatientAdmin(admin.ModelAdmin):  
    list_display = ("patientName", "patientId",)  
    search_fields = ("patientName", "patientId", "patientRecord__ssn")  
    # No direct inlines, because patientRecord is embedded  

