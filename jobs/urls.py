from django.urls import path

from .views import JobView

app_name = 'jobs'

urlpatterns = [
    # Find jobs
    path('', JobView.as_view(), name='jobs_view'),
]