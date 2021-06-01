from django.db import models

class Company(models.Model):
    name=models.CharField(max_length=255, blank=True, null=True)
    address_line_1=models.CharField(max_length=255, blank=True, null=True)
    address_line_2=models.CharField(max_length=255, blank=True, null=True)
    address_town=models.CharField(max_length=255, blank=True, null=True)
    address_region=models.CharField(max_length=255, blank=True, null=True)
    address_country=models.CharField(max_length=255, blank=True, null=True)
    address_zip_code=models.CharField(max_length=255, blank=True, null=True)
    address_industry=models.CharField(max_length=255, blank=True, null=True)
    about=models.TextField(default='')

    def __str__(self):
        return f"{self.name}"
