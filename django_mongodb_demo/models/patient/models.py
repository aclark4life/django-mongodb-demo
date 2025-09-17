from django.db import models
from django_mongodb_backend.models import EmbeddedModel
from django_mongodb_backend.fields import EmbeddedModelField
  

class Billing(EmbeddedModel): 
    cc_type = models.CharField(max_length=50)  
    cc_number = models.CharField(max_length=20)  
  
  
  
class PatientRecord(EmbeddedModel):
    ssn = models.CharField(max_length=11)  # Format: "XXX-XX-XXXX"  
    billing = EmbeddedModelField(  
        Billing  
    )  
    billAmount = models.DecimalField(max_digits=10, decimal_places=2)  
  
  
class Patient(models.Model):  
    patient_name = models.CharField(max_length=255)  
    patient_id = models.BigIntegerField()  
    patient_record = EmbeddedModelField(  
        PatientRecord  
    )  
  
    def __str__(self):  
        return f"{self.patientName} ({self.patientId})"  
