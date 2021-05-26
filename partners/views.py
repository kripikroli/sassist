import os

from datetime import date

from django.contrib.messages.views import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.serializers import serialize
from django.db.models import Q, fields
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, View

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


class PartnerDashboardView(View):

    def get(self, request, *args, **kwargs):

        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)
        context = {
            'partner_user': partner_user,
        }

        return render(request, 'partners/partner_dashboard.html', context)


class PartnerUpdateView(View):

    def get(self, request, *args, **kwargs):


        partner_user_basic = CustomUser.objects.get(id=request.user.id)
        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)
        context = {
            'partner_user_basic': partner_user_basic,
            'partner_user': partner_user,
        }

        return render(request, 'partners/partner_update.html', context)

    def post(self, request, *args, **kwargs):
        
        partner_user_basic = CustomUser.objects.get(id=request.user.id)
        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)

        partner_user_basic.first_name = self.request.POST.get('first_name')
        partner_user_basic.last_name = self.request.POST.get('last_name')

        if self.request.FILES.get('profile_pic', False):
            partner_user.profile_pic = self.request.FILES['profile_pic']

        partner_user.date_of_birth = date(*map(int, self.request.POST.get('date_of_birth').split('-')))
     
        partner_user.phone_number = self.request.POST.get('phone_number')
        partner_user.address_line_1 = self.request.POST.get('address_line_1')
        partner_user.address_line_2 = self.request.POST.get('address_line_2')
        partner_user.address_town = self.request.POST.get('address_town')
        partner_user.address_region = self.request.POST.get('address_region')
        partner_user.address_country = self.request.POST.get('address_country')
        partner_user.address_zip_code = self.request.POST.get('address_zip_code')

        partner_user_basic.save()
        partner_user.save()

        return HttpResponse("Saved")


class PartnerResumePanelView(View):

    def get(self, request, *args, **kwargs):

        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)
        context = {
            'partner_user': partner_user,
        }

        return render(request, 'partners/partner_resume_panel.html', context)


class PartnerEducationView(View):

    def get(self, request, *args, **kwargs):

        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)
        context = {
            'partner_user': partner_user,
            'partner_education': partner_user.partnereducations.all()
        }

        return render(request, 'partners/partner_education.html', context)

    def post(self, request, *args, **kwargs):

        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)

        # PartnerEducation
        pe_degree_type = request.POST.getlist('degree[]')
        pe_school_name = request.POST.getlist('school[]')
        pe_field_name = request.POST.getlist('field[]')
        pe_date_graduated = request.POST.getlist('graduated[]')
        pe_school_address = request.POST.getlist('school_address[]')

        # Saving education
        i = 0
        for degree_type in pe_degree_type:
            education_obj = PartnerEducation(
                degree_type=degree_type,
                school_name=pe_school_name[i],
                field_name=pe_field_name[i],
                date_graduated=pe_date_graduated[i],
                school_address=pe_school_address[i],
                auth_user_id=partner_user
            )
            education_obj.save()
            i += 1

        return HttpResponse("Saved")
