from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import CustomUser, AdminUser, StaffUser, PartnerUser, PatientUser

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type==1:
            AdminUser.objects.create(auth_user_id=instance)
        if instance.user_type==2:
            StaffUser.objects.create(auth_user_id=instance)
        if instance.user_type==3:
            PartnerUser.objects.create(auth_user_id=instance)
        if instance.user_type==4:
            PatientUser.objects.create(auth_user_id=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type==1:
        instance.adminusers.save()
    if instance.user_type==2:
        instance.staffusers.save()
    if instance.user_type==3:
        instance.partnerusers.save()
    if instance.user_type==4:
        instance.patientusers.save()
