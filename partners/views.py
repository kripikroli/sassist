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
        partner_professional_summary = PartnerProfessionalSummary.objects.get(auth_user_id=partner_user.id)
        partner_cover = PartnerCoverLetter.objects.get(auth_user_id=partner_user.id)
        context = {
            'partner_user': partner_user,
            'partner_professional_summary': partner_professional_summary,
            'partner_education': partner_user.partnereducations.all(),
            'partner_licenses': partner_user.partnerlicenses.all(),
            'partner_certifications': partner_user.partnercertifications.all(),
            'partner_skills': partner_user.partnerskills.all(),
            'partner_works': partner_user.partnerworkhistories.all(),
            'partner_references': partner_user.partnerreferences.all(),
            'partner_cover': partner_cover
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


class PartnerLicensesView(View):

    def get(self, request, *args, **kwargs):

        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)
        context = {
            'partner_user': partner_user,
            'partner_licenses': partner_user.partnerlicenses.all()
        }

        return render(request, 'partners/partner_licenses.html', context)

    def post(self, request, *args, **kwargs):

        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)

        # PartnerLicense
        pl_license_name = request.POST.getlist('license_name[]')
        pl_license_code = request.POST.getlist('license_code[]')
        pl_expiration_date = request.POST.getlist('license_expiration_date[]')
        pl_address_acquired = request.POST.getlist('license_address[]')
        pl_is_compact = request.POST.getlist('license_is_compact[]')

        # Saving licenses
        i = 0
        for license_name in pl_license_name:
            license_obj = PartnerLicense(
                license_name=license_name,
                license_code=pl_license_code[i],
                expiration_date=pl_expiration_date[i],
                address_acquired=pl_address_acquired[i],
                is_compact=pl_is_compact[i],
                auth_user_id=partner_user
            )
            license_obj.save()
            i += 1

        return HttpResponse("Saved")


class PartnerCertificationsView(View):

    def get(self, request, *args, **kwargs):

        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)
        context = {
            'partner_user': partner_user,
            'partner_certifications': partner_user.partnercertifications.all()
        }

        return render(request, 'partners/partner_certifications.html', context)

    def post(self, request, *args, **kwargs):

        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)

        # PartnerCertification
        pc_cert_name = request.POST.getlist('certification_name[]')
        pc_cert_code = request.POST.getlist('certification_code[]')
        pc_expiration_date = request.POST.getlist('certification_expiration_date[]')
        pc_address_acquired = request.POST.getlist('certification_address[]')

        # Saving certifications
        i = 0
        for cert_name in pc_cert_name:
            cert_obj = PartnerCertification(
                cert_name=cert_name,
                cert_code=pc_cert_code[i],
                expiration_date=pc_expiration_date[i],
                address_acquired=pc_address_acquired[i],
                auth_user_id=partner_user
            )
            cert_obj.save()
            i += 1

        return HttpResponse("Saved")


class PartnerReferencesView(View):

    def get(self, request, *args, **kwargs):

        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)
        context = {
            'partner_user': partner_user,
            'partner_references': partner_user.partnerreferences.all()
        }

        return render(request, 'partners/partner_references.html', context)

    def post(self, request, *args, **kwargs):

        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)

        # PartnerReference
        pr_name = request.POST.getlist('reference_name[]')
        pr_position = request.POST.getlist('reference_position[]')
        pr_phone_number = request.POST.getlist('reference_phone_number[]')
        pr_email = request.POST.getlist('reference_email[]')
        pr_office_name = request.POST.getlist('reference_office_name[]')
        pr_office_address = request.POST.getlist('reference_office_address[]')
        pr_start_date = request.POST.getlist('reference_start_date[]')
        pr_end_date = request.POST.getlist('reference_end_date[]')

        # Saving references
        i = 0
        for reference in pr_name:
            reference_obj = PartnerReference(
                name=reference,
                position=pr_position[i],
                phone_number=pr_phone_number[i],
                email=pr_email[i],
                office_name=pr_office_name[i],
                office_address=pr_office_address[i],
                start_date=pr_start_date[i],
                end_date=pr_end_date[i],
                auth_user_id=partner_user
            )
            reference_obj.save()
            i += 1

        return HttpResponse("Saved")


class PartnerSkillsView(View):

    def get(self, request, *args, **kwargs):

        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)
        context = {
            'partner_user': partner_user,
            'partner_skills': partner_user.partnerskills.all()
        }

        return render(request, 'partners/partner_skills.html', context)

    def post(self, request, *args, **kwargs):

        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)

        # PartnerSkill
        ps_skills = request.POST.get('skills')

        return HttpResponse("Saved")


class PartnerWorkExperiencesView(View):

    def get(self, request, *args, **kwargs):

        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)
        context = {
            'partner_user': partner_user,
            'partner_work_experiences': partner_user.partnerworkhistories.all()
        }

        return render(request, 'partners/partner_work_experiences.html', context)

    def post(self, request, *args, **kwargs):

        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)

        # PartnerWorkHistory - 1
        work_designation_1 = request.POST.get('work_designation_1', None)
        work_phone_number_1 = request.POST.get('work_phone_number_1', None)
        work_email_1 = request.POST.get('work_email_1', None)
        work_office_name_1 = request.POST.get('work_office_name_1', None)
        work_office_address_1 = request.POST.get('work_office_address_1', None)
        work_start_date_1 = request.POST.get('work_start_date_1', None)
        work_end_date_1 = request.POST.get('work_end_date_1', None)
        work_responsibilities_1 = request.POST.get('work_responsibility_1', None)

        work_r_1 = "".join(work_responsibilities_1.splitlines())
        work_r_1 = work_r_1.replace("\"", "\'")

        # PartnerWorkHistory - 2
        work_designation_2 = request.POST.get('work_designation_2', None)
        work_phone_number_2 = request.POST.get('work_phone_number_2', None)
        work_email_2 = request.POST.get('work_email_2', None)
        work_office_name_2 = request.POST.get('work_office_name_2', None)
        work_office_address_2 = request.POST.get('work_office_address_2', None)
        work_start_date_2 = request.POST.get('work_start_date_2', None)
        work_end_date_2 = request.POST.get('work_end_date_2', None)
        work_responsibilities_2 = request.POST.get('work_responsibility_2', None)

        work_r_2 = "".join(work_responsibilities_2.splitlines())
        work_r_2 = work_r_2.replace("\"", "\'")

        # PartnerWorkHistory - 3
        work_designation_3 = request.POST.get('work_designation_3', None)
        work_phone_number_3 = request.POST.get('work_phone_number_3', None)
        work_email_3 = request.POST.get('work_email_3', None)
        work_office_name_3 = request.POST.get('work_office_name_3', None)
        work_office_address_3 = request.POST.get('work_office_address_3', None)
        work_start_date_3 = request.POST.get('work_start_date_3', None)
        work_end_date_3 = request.POST.get('work_end_date_3', None)
        work_responsibilities_3 = request.POST.get('work_responsibility_3', None)

        work_r_3 = "".join(work_responsibilities_3.splitlines())
        work_r_3 = work_r_3.replace("\"", "\'")

        # Saving work history 1

        if work_designation_1 == None and work_phone_number_1 == None and work_email_1 == None:
            work_history_1_obj = PartnerWorkHistory(
                designation='',
                phone_number='',
                email='',
                office_name='',
                office_address='',
                start_date='',
                end_date='',
                responsibilities='',
                auth_user_id=partner_user,
            )
            work_history_1_obj.save()

        else:
            work_history_1_obj = PartnerWorkHistory(
                designation=work_designation_1,
                phone_number=work_phone_number_1,
                email=work_email_1,
                office_name=work_office_name_1,
                office_address=work_office_address_1,
                start_date=work_start_date_1,
                end_date=work_end_date_1,
                responsibilities=work_r_1,
                auth_user_id=partner_user,
            )
            work_history_1_obj.save()


        # Saving work history 2
        if work_designation_2 == None and work_phone_number_2 == None and work_email_2 == None:
            work_history_2_obj = PartnerWorkHistory(
                designation='',
                phone_number='',
                email='',
                office_name='',
                office_address='',
                start_date='',
                end_date='',
                responsibilities='',
                auth_user_id=partner_user,
            )
            work_history_2_obj.save()

        else:
            work_history_2_obj = PartnerWorkHistory(
                designation=work_designation_2,
                phone_number=work_phone_number_2,
                email=work_email_2,
                office_name=work_office_name_2,
                office_address=work_office_address_2,
                start_date=work_start_date_2,
                end_date=work_end_date_2,
                responsibilities=work_r_2,
                auth_user_id=partner_user,
            )
            work_history_2_obj.save()

        # Saving work history 3
        if work_designation_3 == None and work_phone_number_3 == None and work_email_3 == None:
            work_history_3_obj = PartnerWorkHistory(
                designation='',
                phone_number='',
                email='',
                office_name='',
                office_address='',
                start_date='',
                end_date='',
                responsibilities='',
                auth_user_id=partner_user,
            )
            work_history_3_obj.save()
        
        else:
            work_history_3_obj = PartnerWorkHistory(
            designation=work_designation_3,
            phone_number=work_phone_number_3,
            email=work_email_3,
            office_name=work_office_name_3,
            office_address=work_office_address_3,
            start_date=work_start_date_3,
            end_date=work_end_date_3,
            responsibilities=work_r_3,
            auth_user_id=partner_user,
            )
            work_history_3_obj.save()

        return HttpResponse("Saved")


class PartnerProfessionalSummaryView(View):

    def get(self, request, *args, **kwargs):

        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)
        context = {
            'partner_user': partner_user,
            'partner_professional_summary': partner_user.partnerprofessionalsummaries.all()
        }

        return render(request, 'partners/partner_professional_summary.html', context)

    def post(self, request, *args, **kwargs):

        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)

        # PartnerProfessionalSummary
        professional_summary = request.POST.get('professional_summary')
        summary = "".join(professional_summary.splitlines())
        summary = summary.replace("\"", "\'")

        #Saving professional summary
        professional_summary_obj = PartnerProfessionalSummary(summary=summary, auth_user_id=partner_user)
        professional_summary_obj.save()

        return HttpResponse("Saved")


class PartnerMediaUpload(View):

    def get(self, request, *args, **kwargs):

        remove_file_ed = self.request.GET.get('remove_ed', None)
        remove_file_lc = self.request.GET.get('remove_lc', None)
        remove_file_od = self.request.GET.get('remove_od', None)

        if remove_file_ed:
            try:
                PartnerEducationMedia.objects.get(id=remove_file_ed).delete()
            except:
                pass

        if remove_file_lc:
            try:
                PartnerLCMedia.objects.get(id=remove_file_lc).delete()
            except:
                pass

        if remove_file_od:
            try:
                PartnerOtherMedia.objects.get(id=remove_file_od).delete()
            except:
                pass

        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)
        partner_education_media = PartnerEducationMedia.objects.filter(auth_user_id=partner_user)
        partner_lc_media = PartnerLCMedia.objects.filter(auth_user_id=partner_user)
        partner_other_media = PartnerOtherMedia.objects.filter(auth_user_id=partner_user)

        context = {
            "partner_user": partner_user,
            "partner_education_media": partner_education_media,
            "partner_lc_media": partner_lc_media,
            "partner_other_media": partner_other_media
        }

        return render(request, 'partners/partner_media_upload.html', context)

def educ_media_upload_view(request):
    if request.method == 'POST':
        media_file_name = request.FILES.get('file').name
        media_file = request.FILES.get('file')

        # TODO: hash the file size for extra validation in duplication
        file_format = ''

        if media_file_name.endswith('.jpg') or media_file_name.endswith('.jpeg'):
            file_format = 1
        if media_file_name.endswith('.png'):
            file_format = 2
        if media_file_name.endswith('.pdf'):
            file_format = 3
        
        partner_id = request.POST.get('partner_id')
        partner_instance = PartnerUser.objects.get(id=partner_id)
        obj, created = PartnerEducationMedia.objects.get_or_create(auth_user_id=partner_instance, media_filename=media_file_name, media_format=file_format)

        if created:
            obj.media_content = media_file
            obj.save()

            qs_ed = PartnerEducationMedia.objects.filter(auth_user_id=partner_instance)
            qs_lc = PartnerLCMedia.objects.filter(auth_user_id=partner_instance)
            qs_od = PartnerOtherMedia.objects.filter(auth_user_id=partner_instance)
            data_ed = serialize("json", qs_ed, fields=('id', 'media_filename', 'media_format', 'media_content', 'created'))
            data_lc = serialize("json", qs_lc, fields=('id', 'media_filename', 'media_format', 'media_content', 'created'))
            data_od = serialize("json", qs_od, fields=('id', 'media_filename', 'media_format', 'media_content', 'created'))

            return JsonResponse({'ex': False, 'data_ed': data_ed, 'data_lc': data_lc, 'data_od': data_od})
        
        else:

            qs_ed = PartnerEducationMedia.objects.filter(auth_user_id=partner_instance)
            qs_lc = PartnerLCMedia.objects.filter(auth_user_id=partner_instance)
            qs_od = PartnerOtherMedia.objects.filter(auth_user_id=partner_instance)
            data_ed = serialize("json", qs_ed, fields=('id', 'media_filename', 'media_format', 'media_content', 'created'))
            data_lc = serialize("json", qs_lc, fields=('id', 'media_filename', 'media_format', 'media_content', 'created'))
            data_od = serialize("json", qs_od, fields=('id', 'media_filename', 'media_format', 'media_content', 'created'))

            return JsonResponse({'ex': True, 'data_ed': data_ed, 'data_lc': data_lc, 'data_od': data_od})

    return HttpResponse()


def lc_media_upload_view(request):
    if request.method == 'POST':
        media_file_name = request.FILES.get('file').name
        media_file = request.FILES.get('file')

        # TODO: hash the file size for extra validation in duplication
        file_format = ''

        if media_file_name.endswith('.jpg') or media_file_name.endswith('.jpeg'):
            file_format = 1
        if media_file_name.endswith('.png'):
            file_format = 2
        if media_file_name.endswith('.pdf'):
            file_format = 3
        
        partner_id = request.POST.get('partner_id')
        partner_instance = PartnerUser.objects.get(id=partner_id)
        obj, created = PartnerLCMedia.objects.get_or_create(auth_user_id=partner_instance, media_filename=media_file_name, media_format=file_format)

        if created:
            obj.media_content = media_file
            obj.save()

            qs_ed = PartnerEducationMedia.objects.filter(auth_user_id=partner_instance)
            qs_lc = PartnerLCMedia.objects.filter(auth_user_id=partner_instance)
            qs_od = PartnerOtherMedia.objects.filter(auth_user_id=partner_instance)
            data_ed = serialize("json", qs_ed, fields=('id', 'media_filename', 'media_format', 'media_content', 'created'))
            data_lc = serialize("json", qs_lc, fields=('id', 'media_filename', 'media_format', 'media_content', 'created'))
            data_od = serialize("json", qs_od, fields=('id', 'media_filename', 'media_format', 'media_content', 'created'))

            return JsonResponse({'ex': False, 'data_ed': data_ed, 'data_lc': data_lc, 'data_od': data_od})
        
        else:

            qs_ed = PartnerEducationMedia.objects.filter(auth_user_id=partner_instance)
            qs_lc = PartnerLCMedia.objects.filter(auth_user_id=partner_instance)
            qs_od = PartnerOtherMedia.objects.filter(auth_user_id=partner_instance)
            data_ed = serialize("json", qs_ed, fields=('id', 'media_filename', 'media_format', 'media_content', 'created'))
            data_lc = serialize("json", qs_lc, fields=('id', 'media_filename', 'media_format', 'media_content', 'created'))
            data_od = serialize("json", qs_od, fields=('id', 'media_filename', 'media_format', 'media_content', 'created'))

            return JsonResponse({'ex': True, 'data_ed': data_ed, 'data_lc': data_lc, 'data_od': data_od})

    return HttpResponse()

def other_media_upload_view(request):
    if request.method == 'POST':
        media_file_name = request.FILES.get('file').name
        media_file = request.FILES.get('file')

        # TODO: hash the file size for extra validation in duplication
        file_format = ''

        if media_file_name.endswith('.jpg') or media_file_name.endswith('.jpeg'):
            file_format = 1
        if media_file_name.endswith('.png'):
            file_format = 2
        if media_file_name.endswith('.pdf'):
            file_format = 3
        
        partner_id = request.POST.get('partner_id')
        partner_instance = PartnerUser.objects.get(id=partner_id)
        obj, created = PartnerOtherMedia.objects.get_or_create(auth_user_id=partner_instance, media_filename=media_file_name, media_format=file_format)

        if created:
            obj.media_content = media_file
            obj.save()

            qs_ed = PartnerEducationMedia.objects.filter(auth_user_id=partner_instance)
            qs_lc = PartnerLCMedia.objects.filter(auth_user_id=partner_instance)
            qs_od = PartnerOtherMedia.objects.filter(auth_user_id=partner_instance)
            data_ed = serialize("json", qs_ed, fields=('id', 'media_filename', 'media_format', 'media_content', 'created'))
            data_lc = serialize("json", qs_lc, fields=('id', 'media_filename', 'media_format', 'media_content', 'created'))
            data_od = serialize("json", qs_od, fields=('id', 'media_filename', 'media_format', 'media_content', 'created'))

            return JsonResponse({'ex': False, 'data_ed': data_ed, 'data_lc': data_lc, 'data_od': data_od})
        
        else:

            qs_ed = PartnerEducationMedia.objects.filter(auth_user_id=partner_instance)
            qs_lc = PartnerLCMedia.objects.filter(auth_user_id=partner_instance)
            qs_od = PartnerOtherMedia.objects.filter(auth_user_id=partner_instance)
            data_ed = serialize("json", qs_ed, fields=('id', 'media_filename', 'media_format', 'media_content', 'created'))
            data_lc = serialize("json", qs_lc, fields=('id', 'media_filename', 'media_format', 'media_content', 'created'))
            data_od = serialize("json", qs_od, fields=('id', 'media_filename', 'media_format', 'media_content', 'created'))

            return JsonResponse({'ex': True, 'data_ed': data_ed, 'data_lc': data_lc, 'data_od': data_od})

    return HttpResponse()
