from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import login_view, logout_view


urlpatterns = [
    path('admin/', admin.site.urls),

    # Login
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),

    path('crm/', include('crm.urls', namespace='crm')),
    path('partners/', include('partners.urls', namespace='partners')),
    path('jobs/', include('jobs.urls', namespace='jobs')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)