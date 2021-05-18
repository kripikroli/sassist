from django.urls import path
from .views import (
    admin_dashboard_view, 
    login_view,
    logout_view,
    UserPartnerCreateView,
    UserPartnerListView,
    UserPartnerUpdateView,
    UserPartnerResumeCreateView,
    UserPartnerResumeUpdateView,
)

app_name = 'crm'

urlpatterns = [

    # Dashboard
    path('admin/dashboard/', admin_dashboard_view, name='admin_dashboard_view'),

    # Login
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),

    path('admin/partner_create/', UserPartnerCreateView.as_view(), name='admin_partner_create_view'),
    path('admin/partner_update/<slug:pk>/', UserPartnerUpdateView.as_view(), name='admin_partner_update_view'),
    path('admin/partner_list/', UserPartnerListView.as_view(), name='admin_partner_list_view'),
    path('admin/partner_resume_create/<slug:pk>/', UserPartnerResumeCreateView.as_view(), name='admin_partner_resume_create_view'),
    path('admin/partner_resume_update/<slug:pk>/', UserPartnerResumeUpdateView.as_view(), name='admin_partner_resume_update_view'),

]