from django.urls import path

from .views import (
    PartnerDashboardView,
    PartnerUpdateView,
    PartnerResumePanelView,
    PartnerEducationView,
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

]