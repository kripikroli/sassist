from datetime import datetime, timedelta

from django.shortcuts import render
from django.views.generic import View, ListView
from django.urls import resolve

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Job, JobDescription, JobDetail, JobAbout, JobKeyAbout
from profiles.models import PartnerUser

class JobView(View):
    # TODO: residency_requirement filter

    def get(self, request, *args, **kwargs):

        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)
        job_list = Job.objects.all()

        current_url = request.META['QUERY_STRING']

        job_id = request.GET.get('job_id', None)
        page = request.GET.get('page', 1)

        from_age_param = request.GET.get('fromage', None)
        remote_param = request.GET.get('remote', None)

        if from_age_param:
            # TODO: need a filter for last date visited
            job_list = job_list.filter(created__gte=datetime.today()-timedelta(days=int(from_age_param)))

        job_info = None
        job_description = None
        job_details = None
        job_abouts = None
        job_key_about = None
        abouts = None

        if job_id:
            job_info = Job.objects.get(id=job_id)
            job_description = JobDescription.objects.get(job_id=job_id)
            job_details = JobDetail.objects.filter(job_id=job_id)
            job_abouts = JobAbout.objects.filter(job_id=job_id).values('job_key_about_id').distinct()
            job_key_about = JobKeyAbout.objects.all()
            abouts = JobAbout.objects.filter(job_id=job_id)

        paginator = Paginator(job_list, 10)

        try:
            jobs = paginator.page(page)
        except PageNotAnInteger:
            jobs = paginator.page(1)
        except EmptyPage:
            jobs = paginator.page(paginator.num_pages)

        context = {
            'partner_user': partner_user,
            'jobs': jobs,
            'job_info': job_info,
            'job_description': job_description,
            'job_details': job_details,
            'job_abouts': job_abouts,
            'job_key_about': job_key_about,
            'abouts': abouts,
            'job_id': job_id
        }


        return render(request, 'jobs/main.html', context)

    def post(self, request, *args, **kwargs):
        pass
