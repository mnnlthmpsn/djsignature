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