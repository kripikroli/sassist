from django.db import models
from companies.models import Company

class Job(models.Model):
    title=models.CharField(max_length=255, blank=True, null=True)
    salary=models.FloatField()
    number_to_hire=models.CharField(max_length=255, blank=True, null=True)
    company_id=models.ForeignKey(Company, related_name='companyjobs', on_delete=models.CASCADE)
    short_description=models.TextField(default='')
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


