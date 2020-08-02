from django.db import models
from jsignature.mixins import JSignatureFieldsMixin


class Client(models.Model):
    client = models.CharField(max_length=100, null=False, default='user')

    def __str__(self):
        return self.client

class JSignatureModel(JSignatureFieldsMixin):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    signature_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.signature_date

class Consultation(models.Model):
    client_signature = models.OneToOneField(JSignatureModel, on_delete=models.CASCADE)
    consultation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.consultation_date




class Questionnaire(models.Model):

    CLINICALLY_VULNERABLE_LIST = [
    ('AGE', '65 or older'),
    ('RC', 'Respiratory Conditions'),
    ('HC', 'Heart Conditions'),
    ('CI', 'Compromise or Suppressed Immunity'),
    ('SO', 'Severe Obesity'),
    ('DB', 'Diabetes'),
    ('CKD', 'Chronic Kidney Disease'),
    ('CR', 'Cancer'),
    ('PHD', 'Pregnant Women with Specific Heart Disease'),
    ('RD', 'Rare Diseases')
    ]

    client = models.CharField(max_length=100, blank=False, null=True)
    client_temp = models.IntegerField()
    has_mask = models.BooleanField(default=False, blank=False, null=True)
    covid_diagnosed = models.BooleanField(default=False, blank=False, null=True)
    covid_test_type = models.TextField(blank=False, null=True)
    covid_test_date = models.DateTimeField(blank=False, null=True)
    covid_test_results = models.TextField(blank=False, null=True)
    has_symptoms = models.BooleanField(default=False, blank=False, null=True)
    has_been_to_high_risk_zone = models.BooleanField(default=False, blank=False, null=True)
    has_close_contact_with_suspect = models.BooleanField(default=False, blank=False, null=True)
    is_clinically_vulnerable = models.BooleanField(default=False, blank=False, null=True)
    has_vulnerable_disease = models.BooleanField(
        default=False, blank=False, null=True
    )
    self_quarantine = models.BooleanField(default=False, blank=False, null=True)
    has_traveled = models.BooleanField(default=False, blank=False, null=True)
    had_symptoms = models.BooleanField(default=False, blank=False, null=True)
    client_questions = models.TextField(blank=False, null=True)
    report_agreement = models.BooleanField(default=False, blank=False, null=True)
    
    def __str__(self):
        return self.client