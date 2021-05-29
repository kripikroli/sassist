from django.urls import path

from .views import (
    educ_media_upload_view,
    lc_media_upload_view,
    other_media_upload_view,
    PartnerDashboardView,
    PartnerUpdateView,
    PartnerResumePanelView,
    PartnerEducationView,
    PartnerLicensesView,
    PartnerCertificationsView,
    PartnerReferencesView,
    PartnerSkillsView,
    PartnerWorkExperiencesView,
    PartnerProfessionalSummaryView,
    PartnerCoverLetterView,
    PartnerMediaUpload,
)

app_name = 'partners'

urlpatterns = [

    # Dashboard
    path('dashboard/', PartnerDashboardView.as_view(), name='partner_dashboard_view'),

    # Media upload functions
    path('educ_media_upload/', educ_media_upload_view, name='educ_media_upload'),
    path('lc_media_upload/', lc_media_upload_view, name='lc_media_upload'),
    path('other_media_upload/', other_media_upload_view, name='other_media_upload'),

    # Update partner
    path('account/update/', PartnerUpdateView.as_view(), name='partner_account_update_view'),

    # Resume panel
    path('resume-panel/', PartnerResumePanelView.as_view(), name='partner_resume_panel_view'),

    path('my-education/', PartnerEducationView.as_view(), name='partner_education_view'),
    path('my-licenses/', PartnerLicensesView.as_view(), name='partner_licenses_view'),
    path('my-certifications/', PartnerCertificationsView.as_view(), name='partner_certifications_view'),
    path('my-references/', PartnerReferencesView.as_view(), name='partner_references_view'),
    path('my-skills/', PartnerSkillsView.as_view(), name='partner_skills_view'),
    path('my-work-experiences/', PartnerWorkExperiencesView.as_view(), name='partner_work_experiences_view'),
    path('my-professional-summary/', PartnerProfessionalSummaryView.as_view(), name='partner_professional_summary_view'),
    path('my-cover-letter/', PartnerCoverLetterView.as_view(), name='partner_cover_letter_view'),
    path('my-documents/', PartnerMediaUpload.as_view(), name='partner_media_upload_view'),

]