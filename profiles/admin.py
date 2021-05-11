from django.contrib import admin
from .models import CustomUser, AdminUser, StaffUser, PartnerUser, PatientUser

admin.site.register(CustomUser)
admin.site.register(AdminUser)
admin.site.register(StaffUser)
admin.site.register(PartnerUser)
admin.site.register(PatientUser)
