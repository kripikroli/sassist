from django.urls import path

from .views import (
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
)

app_name = 'partners'

urlpatterns = [

    # Dashboard
    path('dashboard/', PartnerDashboardView.as_view(), name='partner_dashboard_view'),

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

]