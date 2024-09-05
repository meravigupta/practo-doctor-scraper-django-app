from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    address = models.CharField(max_length=500)  # Ensure max_length is sufficient
    postal_code = models.CharField(max_length=20)
    address_region = models.CharField(max_length=255)
    address_locality = models.CharField(max_length=255)
    address_country = models.CharField(max_length=255)


    def __str__(self):
        return self.name
