from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES=((1, "Admin"), (2, "Staff"), (3, "Partner"), (4, "Patient"))
    user_type=models.IntegerField(choices=USER_TYPE_CHOICES, default=1)


class AdminUser(models.Model):
    profile_pic=models.ImageField(upload_to='avatars', default='no_photo.png')
    auth_user_id=models.OneToOneField(CustomUser, related_name='adminusers', on_delete=models.CASCADE)
    bio=models.TextField(default="no bio...")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Admin: {self.auth_user_id}"


class StaffUser(models.Model):
    profile_pic=models.ImageField(upload_to='avatars', default='no_photo.png')
    auth_user_id=models.OneToOneField(CustomUser, related_name='staffusers', on_delete=models.CASCADE)
    bio=models.TextField(default="no bio...")
    is_added_by_admin=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Staff: {self.auth_user_id}"


class PartnerUser(models.Model):
    profile_pic=models.ImageField(upload_to='avatars', default='no_photo.png')
    auth_user_id=models.OneToOneField(CustomUser, related_name='partnerusers', on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address_line_1=models.CharField(max_length=255, null=True, blank=True)
    address_line_2=models.CharField(max_length=255, null=True, blank=True)
    address_town=models.CharField(max_length=120, null=True, blank=True)
    address_region=models.CharField(max_length=120, null=True, blank=True)
    address_country=models.CharField(max_length=120, null=True, blank=True)
    address_zip_code=models.CharField(max_length=20, null=True, blank=True)
    progress_mark=models.IntegerField(default=20)
    is_added_by_admin=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Partner: {self.auth_user_id}"


class PatientUser(models.Model):
    profile_pic=models.ImageField(upload_to='avatars', default='no_photo.png')
    auth_user_id=models.OneToOneField(CustomUser, related_name='patientusers', on_delete=models.CASCADE)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address_line_1=models.CharField(max_length=255, null=True, blank=True)
    address_line_2=models.CharField(max_length=255, null=True, blank=True)
    address_town=models.CharField(max_length=120, null=True, blank=True)
    address_region=models.CharField(max_length=120, null=True, blank=True)
    address_country=models.CharField(max_length=120, null=True, blank=True)
    address_zip_code=models.CharField(max_length=20, null=True, blank=True)
    is_added_by_admin=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Patient: {self.auth_user_id}"
