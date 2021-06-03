from django.db import models
from django.db.models.base import Model
from companies.models import Company

class JobSpecialty(models.Model):
    title=models.CharField(max_length=255)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

class JobLicense(models.Model):
    code=models.CharField(max_length=120)
    name=models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class JobShift(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"

class Job(models.Model):
    REMOTE_CHOICES=(
        (1, 'Not Remote'),
        (2, 'Partial Remote'),
        (3, 'Full Remote'),
        (5, 'Multiple Options'),
        (6, 'Unspecified')
    )
    SALARY_PER_HOUR_CHOICES=(
        (1, '$10.00+ /hour'),
        (2, '$12.50+ /hour'),
        (3, '$15.00+ /hour'),
        (4, '$17.50+ /hour'),
        (5, '$20.00+ /hour'),
        (6, '$22.50+ /hour'),
        (7, '$25.00+ /hour'),
        (8, '$27.50+ /hour'),
        (9, '$30.00+ /hour'),
        (10, '$32.50+ /hour'),
        (11, '$35.00+ /hour'),
        (12, '$37.50+ /hour'),
        (13, '$40.00+ /hour'),
        (14, '$42.50+ /hour'),
        (15, '$45.00+ /hour'),
        (16, '$47.50+ /hour'),
        (17, '$50.00+ /hour'),
        (18, '$52.50+ /hour'),
        (19, '$55.00+ /hour'),
        (20, 'Unspecified')
    )
    JOB_TYPE_CHOICES=(
        (1, 'Full-time'),
        (2, 'Part-time'),
        (3, 'Contract'),
        (4, 'Temporary'),
        (5, 'Per Diem'),
        (6, 'Multiple Options'),
        (7, 'Unspecified')
    )

    EXP_LEVEL_CHOICES=(
        (1, 'Entry Level'),
        (2, 'Mid Level'),
        (3, 'Expert Level')
    )

    title=models.CharField(max_length=255, blank=True, null=True)
    salary=models.FloatField()
    number_to_hire=models.CharField(max_length=255, blank=True, null=True)
    company_id=models.ForeignKey(Company, related_name='companyjobs', on_delete=models.CASCADE)
    short_description=models.TextField(default='')
    remote_option=models.IntegerField(choices=REMOTE_CHOICES, default=1)
    salary_per_hour_option=models.IntegerField(choices=SALARY_PER_HOUR_CHOICES, default=1)
    job_type_option=models.IntegerField(choices=JOB_TYPE_CHOICES, default=1)
    exp_level_option=models.IntegerField(choices=EXP_LEVEL_CHOICES, default=1)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


class JobKeyAbout(models.Model):
    key_title=models.CharField(max_length=255, blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.key_title}"


class JobKeyDetail(models.Model):
    key_title=models.CharField(max_length=255, blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.key_title}"


class JobAbout(models.Model):
    about=models.CharField(max_length=255, blank=True, null=True)
    job_id=models.ForeignKey(Job, related_name='jobabouts', on_delete=models.CASCADE)
    job_key_about_id=models.ForeignKey(JobKeyAbout, related_name='jobkeyabouts', on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.about}"


class JobDetail(models.Model):
    detail=models.CharField(max_length=255, blank=True, null=True)
    job_id=models.ForeignKey(Job, related_name='jobdetails', on_delete=models.CASCADE)
    job_key_detail_id=models.ForeignKey(JobKeyDetail, related_name='jobkeydetails', on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.detail}"


class JobDescription(models.Model):
    short_description=models.TextField(default='')
    full_description=models.TextField(default='')
    job_id=models.ForeignKey(Job, related_name='jobdescriptions', on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.short_description}"


