from django.urls import path

from .views import (
    PartnerDashboardView,
    PartnerUpdateView,
)

app_name = 'partners'

urlpatterns = [

    # Dashboard
    path('dashboard/', PartnerDashboardView.as_view(), name='partner_dashboard_view'),

    # Update partner
    path('account/update/', PartnerUpdateView.as_view(), name='partner_account_update_view'),

]