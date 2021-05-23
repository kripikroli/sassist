from django.contrib import admin
from .models import (
    PartnerEducation,
    PartnerLicense,
    PartnerCertification,
    PartnerReference,
    PartnerSkill,
    PartnerCoverLetter,
    PartnerEducationMedia,
    PartnerLCMedia,
    PartnerOtherMedia,
    PartnerProfessionalSummary,
    PartnerWorkHistory
)

admin.site.register(PartnerEducation)
admin.site.register(PartnerLicense)
admin.site.register(PartnerCertification)
admin.site.register(PartnerReference)
admin.site.register(PartnerSkill)
admin.site.register(PartnerCoverLetter)
admin.site.register(PartnerEducationMedia)
admin.site.register(PartnerLCMedia)
admin.site.register(PartnerOtherMedia)
admin.site.register(PartnerProfessionalSummary)
admin.site.register(PartnerWorkHistory)

