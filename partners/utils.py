from profiles.models import CustomUser, PartnerUser

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
    PartnerWorkHistory,
)

def get_progress_value(id):
    partner_instance = PartnerUser.objects.get(auth_user_id=id)

    progress_mark = 10

    try:
        partner_professional_summary = PartnerProfessionalSummary.objects.get(auth_user_id=partner_instance.id)
    except:
        partner_professional_summary = None

    try:
        partner_cover = PartnerCoverLetter.objects.get(auth_user_id=partner_instance.id)
    except:
        partner_cover = None

    partner_education = partner_instance.partnereducations.all()
    partner_licenses = partner_instance.partnerlicenses.all()
    partner_certifications = partner_instance.partnercertifications.all()
    partner_skills = partner_instance.partnerskills.all()
    partner_works = partner_instance.partnerworkhistories.all()
    partner_references = partner_instance.partnerreferences.all()

    partner_education_media = PartnerEducationMedia.objects.filter(auth_user_id=partner_instance)
    partner_lc_media = PartnerLCMedia.objects.filter(auth_user_id=partner_instance)
    partner_other_media = PartnerOtherMedia.objects.filter(auth_user_id=partner_instance)
    

    if partner_professional_summary:
        progress_mark += 15
    if partner_cover:
        progress_mark += 15
    if len(partner_education) > 0:
        progress_mark += 10
    if len(partner_licenses) > 0:
        progress_mark += 5
    if len(partner_certifications) > 0:
        progress_mark += 5
    if len(partner_skills) > 0:
        progress_mark += 10
    if len(partner_works) > 0:
        progress_mark += 10
    if len(partner_references) > 0:
        progress_mark += 10
    if (len(partner_education_media) > 0 or len(partner_lc_media) > 0 or len(partner_other_media) > 0):
        progress_mark += 10

    return progress_mark