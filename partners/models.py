from datetime import date, timezone

from django.db import models
from profiles.models import PartnerUser

class PartnerEducation(models.Model):
    DEGREE_TYPES = (
        (1, 'Highschool'),
        (2, 'Associate'),
        (3, 'Bachelor'),
        (4, 'Master'),
        (5, 'Doctorate'),
        (6, 'Unspecified'),
    )

    degree_type=models.IntegerField(choices=DEGREE_TYPES, default=1)
    school_name=models.CharField(max_length=255, blank=True, null=True)
    field_name=models.CharField(max_length=255, blank=True, null=True)
    date_graduated=models.CharField(max_length=255, blank=True, null=True)
    school_address=models.CharField(max_length=255, blank=True, null=True)
    file=models.FileField(upload_to='partners', blank=True, null=True)
    is_added_by_admin=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    auth_user_id=models.ForeignKey(PartnerUser, related_name='partnereducations', on_delete=models.CASCADE)

    def __str__(self):
        return self.school_name

    def get_days_ago(self):
        return ((date.today() - self.created.date()).days)


class PartnerEducationMedia(models.Model):
    MEDIA_TYPE_CHOICES=((1,"Image"),)
    MEDIA_FORMAT_CHOICES=((1, "JPG"), (2, "PNG"), (3, "PDF"))
    media_filename=models.CharField(max_length=255, default='no name')
    media_type=models.IntegerField(choices=MEDIA_TYPE_CHOICES, default=1)
    media_format=models.IntegerField(choices=MEDIA_FORMAT_CHOICES, default=1)
    media_content=models.FileField(upload_to='education_files', blank=True)
    is_active=models.IntegerField(default=1)
    is_added_by_admin=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    auth_user_id=models.ForeignKey(PartnerUser, related_name='partnereducationmedias', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.media_filename}"

    def get_date_only(self):
        return f"five"


class PartnerLCMedia(models.Model):
    MEDIA_TYPE_CHOICES=((1,"Image"),)
    MEDIA_FORMAT_CHOICES=((1, "JPG"), (2, "PNG"), (3, "PDF"))
    media_filename=models.CharField(max_length=255, default='no name')
    media_type=models.IntegerField(choices=MEDIA_TYPE_CHOICES, default=1)
    media_format=models.IntegerField(choices=MEDIA_FORMAT_CHOICES, default=1)
    media_content=models.FileField(upload_to='lc_files', blank=True)
    is_active=models.IntegerField(default=1)
    is_added_by_admin=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    auth_user_id=models.ForeignKey(PartnerUser, related_name='partnerlcmedias', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.media_filename}"


class PartnerOtherMedia(models.Model):
    MEDIA_TYPE_CHOICES=((1,"Image"),)
    MEDIA_FORMAT_CHOICES=((1, "JPG"), (2, "PNG"), (3, "PDF"))
    media_filename=models.CharField(max_length=255, default='no name')
    media_type=models.IntegerField(choices=MEDIA_TYPE_CHOICES, default=1)
    media_format=models.IntegerField(choices=MEDIA_FORMAT_CHOICES, default=1)
    media_content=models.FileField(upload_to='other_files', blank=True)
    is_active=models.IntegerField(default=1)
    is_added_by_admin=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    auth_user_id=models.ForeignKey(PartnerUser, related_name='partnerothermedias', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.media_filename}"


class PartnerLicense(models.Model):
    license_name=models.CharField(max_length=255, blank=True, null=True)
    license_code=models.CharField(max_length=255, blank=True, null=True)
    expiration_date=models.CharField(max_length=255, blank=True, null=True)
    address_acquired=models.CharField(max_length=255, blank=True, null=True)
    file=models.FileField(upload_to='partners', blank=True, null=True)
    is_compact = models.CharField(max_length=10, blank=True, null=True)
    is_added_by_admin=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    auth_user_id=models.ForeignKey(PartnerUser, related_name='partnerlicenses', on_delete=models.CASCADE)

    def __str__(self):
        return self.license_name

    def get_days_ago(self):
        return ((date.today() - self.created.date()).days)


class PartnerCertification(models.Model):
    cert_name=models.CharField(max_length=255, blank=True, null=True)
    cert_code=models.CharField(max_length=255, blank=True, null=True)
    expiration_date=models.CharField(max_length=255, blank=True, null=True)
    address_acquired=models.CharField(max_length=255, blank=True, null=True)
    file=models.FileField(upload_to='partners', blank=True, null=True)
    is_added_by_admin=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    auth_user_id=models.ForeignKey(PartnerUser, related_name='partnercertifications', on_delete=models.CASCADE)

    def __str__(self):
        return self.cert_name

    def get_days_ago(self):
        return ((date.today() - self.created.date()).days)

class PartnerReference(models.Model):
    name=models.CharField(max_length=255, blank=True, null=True)
    position=models.CharField(max_length=255, blank=True, null=True)
    phone_number=models.CharField(max_length=255, blank=True, null=True)
    email=models.CharField(max_length=255, blank=True, null=True)
    office_name=models.CharField(max_length=255, blank=True, null=True)
    office_address=models.CharField(max_length=255, blank=True, null=True)
    file=models.FileField(upload_to='partners', blank=True, null=True)
    start_date=models.CharField(max_length=255, blank=True, null=True)
    end_date=models.CharField(max_length=255, blank=True, null=True)
    is_added_by_admin=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    auth_user_id=models.ForeignKey(PartnerUser, related_name='partnerreferences', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_days_ago(self):
        return ((date.today() - self.created.date()).days)


class PartnerSkill(models.Model):
    skill_name=models.CharField(max_length=255, null=True, blank=True)
    is_added_by_admin=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    auth_user_id=models.ForeignKey(PartnerUser, related_name='partnerskills', on_delete=models.CASCADE)

    def __str__(self):
        return self.skill_name

    def get_days_ago(self):
        return ((date.today() - self.created.date()).days)


class PartnerCoverLetter(models.Model):
    letter=models.TextField(default='')
    is_added_by_admin=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    auth_user_id=models.ForeignKey(PartnerUser, related_name='partnercoverletters', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.created}"

    def get_days_ago(self):
        return ((date.today() - self.created.date()).days)


class PartnerProfessionalSummary(models.Model):
    summary=models.TextField(default='')
    is_added_by_admin=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    auth_user_id=models.ForeignKey(PartnerUser, related_name='partnerprofessionalsummaries', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.created}"

    def get_days_ago(self):
        return ((date.today() - self.created.date()).days)


class PartnerWorkHistory(models.Model):
    designation=models.CharField(max_length=255, blank=True, null=True)
    phone_number=models.CharField(max_length=255, blank=True, null=True)
    email=models.CharField(max_length=255, blank=True, null=True)
    office_name=models.CharField(max_length=255, blank=True, null=True)
    office_address=models.CharField(max_length=255, blank=True, null=True)
    start_date=models.CharField(max_length=255, blank=True, null=True)
    end_date=models.CharField(max_length=255, blank=True, null=True)
    is_added_by_admin=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    auth_user_id=models.ForeignKey(PartnerUser, related_name='partnerworkhistories', on_delete=models.CASCADE)

    def __str__(self):
        return self.designation

    def get_days_ago(self):
        return ((date.today() - self.created.date()).days)


class PartnerResponsibility(models.Model):
    position=models.CharField(max_length=255, blank=True, null=True)
    work_history_id=models.ForeignKey(PartnerWorkHistory, related_name='partnerresponsibilities', on_delete=models.CASCADE)

    def __str__(self):
        return self.position

    def get_days_ago(self):
        return ((date.today() - self.created.date()).days)


