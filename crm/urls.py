from django.urls import path
from .views import (
    admin_dashboard_view, 
    login_view,
    logout_view,
    UserPartnerCreateView,
    UserPartnerListView,

)

app_name = 'crm'

urlpatterns = [

    # Dashboard
    path('admin/dashboard/', admin_dashboard_view, name='admin_dashboard_view'),

    # Login
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),

    path('admin/partner_create/', UserPartnerCreateView.as_view(), name='admin_partner_create_view'),
    path('admin/partner_list/', UserPartnerListView.as_view(), name='admin_partner_list_view'),

]