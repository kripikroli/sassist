from django.contrib import admin

from .models import (
    Job,
    JobKeyAbout,
    JobKeyDetail,
    JobAbout,
    JobDetail,
    JobDescription
)

admin.site.register([
    Job, 
    JobKeyAbout,
    JobKeyDetail,
    JobAbout,
    JobDetail,
    JobDescription 
])