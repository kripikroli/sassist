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
from .utils import get_progress_value


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

        progress_mark = 10

        try:
            partner_professional_summary = PartnerProfessionalSummary.objects.get(auth_user_id=partner_user.id)
        except:
            partner_professional_summary = None

        try:
            partner_cover = PartnerCoverLetter.objects.get(auth_user_id=partner_user.id)
        except:
            partner_cover = None

        partner_education = partner_user.partnereducations.all()
        partner_licenses = partner_user.partnerlicenses.all()
        partner_certifications = partner_user.partnercertifications.all()
        partner_skills = partner_user.partnerskills.all()
        partner_works = partner_user.partnerworkhistories.all()
        partner_references = partner_user.partnerreferences.all()
        
        context = {
            'partner_user': partner_user,
            'partner_professional_summary': partner_professional_summary,
            'partner_education': partner_education,
            'partner_licenses': partner_licenses,
            'partner_certifications': partner_certifications,
            'partner_skills': partner_skills,
            'partner_works': partner_works,
            'partner_references': partner_references,
            'partner_cover': partner_cover,
            'progress_mark': get_progress_value(request.user.id)
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

        # Delete skills first
        PartnerSkill.objects.filter(auth_user_id=partner_user).delete()

        # Saving skills
        skill_list = ps_skills.split(',')
        for skill in skill_list:
            if skill != '':
                skill_obj = PartnerSkill(skill_name=skill, auth_user_id=partner_user)
                skill_obj.save()

        return HttpResponse("Saved")


class PartnerWorkExperiencesView(View):

    def get(self, request, *args, **kwargs):

        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)
        work_history_id = request.GET.get('work_id', None)

        if work_history_id:
            partner_work_experiences = PartnerWorkHistory.objects.get(id=work_history_id, auth_user_id=partner_user)
        else:
            partner_work_experiences = None

        context = {
            'partner_user': partner_user,
            'partner_work_experiences': partner_work_experiences
        }

        return render(request, 'partners/partner_work_experiences.html', context)

    def post(self, request, *args, **kwargs):

        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)

        # PartnerWorkHistory
        work_designation = request.POST.get('work_designation', None)
        work_phone_number = request.POST.get('work_phone_number', None)
        work_email = request.POST.get('work_email', None)
        work_office_name = request.POST.get('work_office_name', None)
        work_office_address = request.POST.get('work_office_address', None)
        work_start_date = request.POST.get('work_start_date', None)
        work_end_date = request.POST.get('work_end_date', None)
        work_responsibilities = request.POST.get('work_responsibility', None)
        w_id = request.POST.get('w_id', None)
        delete = request.POST.get('delete', None)

        work_r = "".join(work_responsibilities.splitlines())
        work_r = work_r.replace("\"", "\'")

        # Saving work history

        if w_id != 'blank':
            if delete == 'delete':
                PartnerWorkHistory.objects.get(id=w_id).delete()
            else:
                work_history_obj = PartnerWorkHistory.objects.get(id=w_id)
                work_history_obj.designation = work_designation
                work_history_obj.phone_number = work_phone_number
                work_history_obj.email=work_email
                work_history_obj.office_name=work_office_name
                work_history_obj.office_address=work_office_address
                work_history_obj.start_date=work_start_date
                work_history_obj.end_date=work_end_date
                work_history_obj.responsibilities=work_r
                work_history_obj.auth_user_id=partner_user
                work_history_obj.save()
        else:
            work_history_obj = PartnerWorkHistory(
                designation=work_designation,
                phone_number=work_phone_number,
                email=work_email,
                office_name=work_office_name,
                office_address=work_office_address,
                start_date=work_start_date,
                end_date=work_end_date,
                responsibilities=work_r,
                auth_user_id=partner_user,
            )
            work_history_obj.save()

        return HttpResponse("Saved")


class PartnerProfessionalSummaryView(View):

    def get(self, request, *args, **kwargs):

        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)

        try:
            partner_professional_summary = PartnerProfessionalSummary.objects.get(auth_user_id=partner_user.id)
        except:
            partner_professional_summary = None

        context = {
            'partner_user': partner_user,
            'partner_professional_summary': partner_professional_summary
        }

        return render(request, 'partners/partner_professional_summary.html', context)

    def post(self, request, *args, **kwargs):

        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)

        try:
            partner_professional_summary = PartnerProfessionalSummary.objects.get(auth_user_id=partner_user.id)
        except:
            partner_professional_summary = None
      
        # PartnerProfessionalSummary
        professional_summary = request.POST.get('professional_summary')
        summary = "".join(professional_summary.splitlines())
        summary = summary.replace("\"", "\'")

        if partner_professional_summary:
            #Updating old professional summary
            partner_professional_summary.summary = summary
            partner_professional_summary.auth_user_id = partner_user
            partner_professional_summary.save()
        else:
            #Saving new professional summary
            professional_summary_obj = PartnerProfessionalSummary(summary=summary, auth_user_id=partner_user)
            professional_summary_obj.save()

        return HttpResponse("Saved")


class PartnerCoverLetterView(View):

    def get(self, request, *args, **kwargs):
        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)

        try:
            partner_cover_letter = PartnerCoverLetter.objects.get(auth_user_id=partner_user.id)
        except:
            partner_cover_letter = None

        context = {
            'partner_user': partner_user,
            'partner_cover_letter': partner_cover_letter
        }

        return render(request, 'partners/partner_cover_letter.html', context)

    def post(self, request, *args, **kwargs):

        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)

        try:
            partner_cover_letter = PartnerCoverLetter.objects.get(auth_user_id=partner_user.id)
        except:
            partner_cover_letter = None

        # PartnerCoverLetter
        cover_letter = request.POST.get('cover_letter')
        cover_l = "".join(cover_letter.splitlines())
        cover_l = cover_l.replace("\"", "\'")

        if partner_cover_letter:
            #Updating old cover letter
            partner_cover_letter.letter = cover_l
            partner_cover_letter.auth_user_id = partner_user
            partner_cover_letter.save()
        else:
            #Savin new cover letter
            cover_letter_obj = PartnerCoverLetter(letter=cover_l, auth_user_id=partner_user)
            cover_letter_obj.save()

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
            "partner_other_media": partner_other_media,
            "progress_mark": get_progress_value(request.user.id)
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

            return JsonResponse({'ex': False, 'data_ed': data_ed, 'data_lc': data_lc, 'data_od': data_od, 'pm': get_progress_value(request.user.id)})
        
        else:

            qs_ed = PartnerEducationMedia.objects.filter(auth_user_id=partner_instance)
            qs_lc = PartnerLCMedia.objects.filter(auth_user_id=partner_instance)
            qs_od = PartnerOtherMedia.objects.filter(auth_user_id=partner_instance)
            data_ed = serialize("json", qs_ed, fields=('id', 'media_filename', 'media_format', 'media_content', 'created'))
            data_lc = serialize("json", qs_lc, fields=('id', 'media_filename', 'media_format', 'media_content', 'created'))
            data_od = serialize("json", qs_od, fields=('id', 'media_filename', 'media_format', 'media_content', 'created'))

            return JsonResponse({'ex': True, 'data_ed': data_ed, 'data_lc': data_lc, 'data_od': data_od, 'pm': get_progress_value(request.user.id)})

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

            return JsonResponse({'ex': False, 'data_ed': data_ed, 'data_lc': data_lc, 'data_od': data_od, 'pm': get_progress_value(request.user.id)})
        
        else:

            qs_ed = PartnerEducationMedia.objects.filter(auth_user_id=partner_instance)
            qs_lc = PartnerLCMedia.objects.filter(auth_user_id=partner_instance)
            qs_od = PartnerOtherMedia.objects.filter(auth_user_id=partner_instance)
            data_ed = serialize("json", qs_ed, fields=('id', 'media_filename', 'media_format', 'media_content', 'created'))
            data_lc = serialize("json", qs_lc, fields=('id', 'media_filename', 'media_format', 'media_content', 'created'))
            data_od = serialize("json", qs_od, fields=('id', 'media_filename', 'media_format', 'media_content', 'created'))

            return JsonResponse({'ex': True, 'data_ed': data_ed, 'data_lc': data_lc, 'data_od': data_od, 'pm': get_progress_value(request.user.id)})

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

            return JsonResponse({'ex': False, 'data_ed': data_ed, 'data_lc': data_lc, 'data_od': data_od, 'pm': get_progress_value(request.user.id)})
        
        else:

            qs_ed = PartnerEducationMedia.objects.filter(auth_user_id=partner_instance)
            qs_lc = PartnerLCMedia.objects.filter(auth_user_id=partner_instance)
            qs_od = PartnerOtherMedia.objects.filter(auth_user_id=partner_instance)
            data_ed = serialize("json", qs_ed, fields=('id', 'media_filename', 'media_format', 'media_content', 'created'))
            data_lc = serialize("json", qs_lc, fields=('id', 'media_filename', 'media_format', 'media_content', 'created'))
            data_od = serialize("json", qs_od, fields=('id', 'media_filename', 'media_format', 'media_content', 'created'))

            return JsonResponse({'ex': True, 'data_ed': data_ed, 'data_lc': data_lc, 'data_od': data_od, 'pm': get_progress_value(request.user.id)})

    return HttpResponse()


class PartnerEducationUpdateView(View):

    def get(self, request, *args, **kwargs):
        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)

        p_education = PartnerEducation.objects.filter(auth_user_id=partner_user.id)

        context = {
            "partner_user": partner_user,
            "p_education": p_education,
        }

        return render(request, 'partners/partner_education_update.html', context)

    def post(self, request, *args, **kwargs):
        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)

        # PartnerEducation
        pe_ids = request.POST.getlist('education_id[]')
        pe_degree_type = request.POST.getlist('degree[]')
        pe_school_name = request.POST.getlist('school[]')
        pe_field_name = request.POST.getlist('field[]')
        pe_date_graduated = request.POST.getlist('graduated[]')
        pe_school_address = request.POST.getlist('school_address[]')
        pe_delete = request.POST.getlist('delete[]')

        # Saving education
        i = 0
        for degree_type in pe_degree_type:
            if pe_delete[i] == 'delete':
                PartnerEducation.objects.get(id=pe_ids[i]).delete()
            else:
                education_obj = PartnerEducation.objects.get(id=pe_ids[i])      
                education_obj.degree_type = degree_type
                education_obj.school_name = pe_school_name[i]
                education_obj.field_name = pe_field_name[i]
                education_obj.date_graduated = pe_date_graduated[i]
                education_obj.school_address = pe_school_address[i]
                education_obj.auth_user_id = partner_user
                education_obj.save()
                   
            i += 1

        return HttpResponse("Saved")


class PartnerLicensesUpdateView(View):

    def get(self, request, *args, **kwargs):
        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)

        p_license = PartnerLicense.objects.filter(auth_user_id=partner_user.id)

        context = {
            "partner_user": partner_user,
            "p_license": p_license,
        }

        return render(request, 'partners/partner_licenses_update.html', context)

    def post(self, request, *args, **kwargs):
        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)

        # PartnerLicense
        pl_ids = request.POST.getlist('license_id[]')
        pl_license_name = request.POST.getlist('license_name[]')
        pl_license_code = request.POST.getlist('license_code[]')
        pl_expiration_date = request.POST.getlist('license_expiration_date[]')
        pl_address_acquired = request.POST.getlist('license_address[]')
        pl_is_compact = request.POST.getlist('license_is_compact[]')
        pl_delete = request.POST.getlist('delete[]')

        # Saving licenses
        i = 0
        for license_name in pl_license_name:
            if pl_delete[i] == 'delete':
                PartnerLicense.objects.get(id=pl_ids[i]).delete()
            else:
                license_obj = PartnerLicense.objects.get(id=pl_ids[i])
                license_obj.license_name=license_name
                license_obj.license_code=pl_license_code[i]
                license_obj.expiration_date=pl_expiration_date[i]
                license_obj.address_acquired=pl_address_acquired[i]
                license_obj.is_compact=pl_is_compact[i]
                license_obj.auth_user_id=partner_user
                license_obj.save()
            i += 1

        return HttpResponse("Saved")


class PartnerCertificationsUpdateView(View):

    def get(self, request, *args, **kwargs):
        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)

        p_certification = PartnerCertification.objects.filter(auth_user_id=partner_user.id)

        context = {
            "partner_user": partner_user,
            "p_certification": p_certification,
        }

        return render(request, 'partners/partner_certifications_update.html', context)

    def post(self, request, *args, **kwargs):
        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)

        # PartnerCertification
        pc_ids = request.POST.getlist('certification_id[]')
        pc_cert_name = request.POST.getlist('certification_name[]')
        pc_cert_code = request.POST.getlist('certification_code[]')
        pc_expiration_date = request.POST.getlist('certification_expiration_date[]')
        pc_address_acquired = request.POST.getlist('certification_address[]')
        pc_file = request.FILES.getlist('certification_file[]')
        pc_delete = request.POST.getlist('delete[]')

        # Saving licenses
        i = 0
        for cert_name in pc_cert_name:
            if pc_delete[i] == 'delete':
                PartnerCertification.objects.get(id=pc_ids[i]).delete()
            else:
                cert_obj = PartnerCertification.objects.get(id=pc_ids[i])
                cert_obj.cert_name=cert_name
                cert_obj.cert_code=pc_cert_code[i]
                cert_obj.expiration_date=pc_expiration_date[i]
                cert_obj.address_acquired=pc_address_acquired[i]
                cert_obj.auth_user_id=partner_user
                cert_obj.save()
            i += 1

        return HttpResponse("Saved")


class PartnerReferencesUpdateView(View):

    def get(self, request, *args, **kwargs):
        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)

        p_reference = PartnerReference.objects.filter(auth_user_id=partner_user.id)

        context = {
            "partner_user": partner_user,
            "p_reference": p_reference,
        }

        return render(request, 'partners/partner_references_update.html', context)

    def post(self, request, *args, **kwargs):
        partner_user = PartnerUser.objects.get(auth_user_id=request.user.id)

        # PartnerReference
        pr_ids = request.POST.getlist('reference_id[]')
        pr_name = request.POST.getlist('reference_name[]')
        pr_position = request.POST.getlist('reference_position[]')
        pr_phone_number = request.POST.getlist('reference_phone_number[]')
        pr_email = request.POST.getlist('reference_email[]')
        pr_office_name = request.POST.getlist('reference_office_name[]')
        pr_office_address = request.POST.getlist('reference_office_address[]')
        pr_start_date = request.POST.getlist('reference_start_date[]')
        pr_end_date = request.POST.getlist('reference_end_date[]')
        pr_delete = request.POST.getlist('delete[]')

        # Saving references
        i = 0
        for reference in pr_name:
            if pr_delete[i] == 'delete':
                PartnerReference.objects.get(id=pr_ids[i]).delete()
            else:
                reference_obj = PartnerReference.objects.get(id=pr_ids[i])
                reference_obj.name=reference
                reference_obj.position=pr_position[i]
                reference_obj.phone_number=pr_phone_number[i]
                reference_obj.email=pr_email[i]
                reference_obj.office_name=pr_office_name[i]
                reference_obj.office_address=pr_office_address[i]
                reference_obj.start_date=pr_start_date[i]
                reference_obj.end_date=pr_end_date[i]
                reference_obj.auth_user_id=partner_user
                reference_obj.save()
            i += 1

        return HttpResponse("Saved")




