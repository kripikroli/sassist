from django.contrib import admin
from .models import (
    PartnerEducation,
    PartnerLicense,
    PartnerCertification,
    PartnerReference,
    PartnerSkill,
    PartnerCoverLetter,
)

admin.site.register(PartnerEducation)
admin.site.register(PartnerLicense)
admin.site.register(PartnerCertification)
admin.site.register(PartnerReference)
admin.site.register(PartnerSkill)
admin.site.register(PartnerCoverLetter)

