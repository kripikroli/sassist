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

from partners.models import (
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

def admin_dashboard_view(request):
    return render(request, 'crm/admin_dashboard.html')

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


class UserPartnerCreateView(SuccessMessageMixin, CreateView):

    model = CustomUser
    template_name = 'crm/admin_partner_create.html'
    success_message = 'Partner added successfully!'
    fields = (
        'first_name',
        'last_name',
        'email',
        'username',
        'password',
    )

    def form_valid(self, form):

        user = form.save(commit=False)
        user.is_active = True
        user.user_type = 3
        user.set_password(form.cleaned_data['password'])
        user.save()

        # Saving user.partnerusers
        user.partnerusers.profile_pic = self.request.FILES['profile_pic']
        user.partnerusers.date_of_birth = date(*map(int, self.request.POST.get('date_of_birth').split('-')))
     
        user.partnerusers.phone_number = self.request.POST.get('phone_number')
        user.partnerusers.address_line_1 = self.request.POST.get('address_line_1')
        user.partnerusers.address_line_2 = self.request.POST.get('address_line_2')
        user.partnerusers.address_town = self.request.POST.get('address_town')
        user.partnerusers.address_region = self.request.POST.get('address_region')
        user.partnerusers.address_country = self.request.POST.get('address_country')
        user.partnerusers.address_zip_code = self.request.POST.get('address_zip_code')

        is_added_by_admin = False

        if self.request.POST.get('is_added_by_admin') == 'on':
            is_added_by_admin = True

        user.partnerusers.is_added_by_admin = is_added_by_admin
        user.save()

        messages.success(self.request, 'Partner user created')

        return HttpResponseRedirect(reverse('crm:admin_partner_list_view'))


class UserPartnerUpdateView(SuccessMessageMixin, UpdateView):

    model = CustomUser
    template_name = 'crm/admin_partner_update.html'
    success_message = 'Partner updated successfully!'
    fields = (
        'first_name',
        'last_name',
        'email',
        'username',
        'password',
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['partneruser'] = PartnerUser.objects.get(auth_user_id=self.object.pk)
        return context

    def form_valid(self, form):

        user = form.save(commit=False)
        user.is_active = True
        user.user_type = 3
        user.set_password(form.cleaned_data['password'])
        user.save()

        # Saving user.partnerusers
        partneruser = PartnerUser.objects.get(auth_user_id=user.id)

        if self.request.FILES.get('profile_pic', False):
            partneruser.profile_pic = self.request.FILES['profile_pic']

        partneruser.date_of_birth = date(*map(int, self.request.POST.get('date_of_birth').split('-')))
     
        partneruser.phone_number = self.request.POST.get('phone_number')
        partneruser.address_line_1 = self.request.POST.get('address_line_1')
        partneruser.address_line_2 = self.request.POST.get('address_line_2')
        partneruser.address_town = self.request.POST.get('address_town')
        partneruser.address_region = self.request.POST.get('address_region')
        partneruser.address_country = self.request.POST.get('address_country')
        partneruser.address_zip_code = self.request.POST.get('address_zip_code')

        is_added_by_admin = False

        if self.request.POST.get('is_added_by_admin') == 'on':
            is_added_by_admin = True

        partneruser.is_added_by_admin = is_added_by_admin
        partneruser.save()

        messages.success(self.request, 'Partner user updated')

        return HttpResponseRedirect(reverse('crm:admin_partner_list_view'))


class UserPartnerListView(ListView):

    model = CustomUser
    fields = '__all__'
    template_name = 'crm/admin_partner_list.html'

    # Number of partners to paginate
    paginate_by = 10

    def get_queryset(self):

        filter_val = self.request.GET.get('filter', '')
        order_by = self.request.GET.get('orderby', 'id')

        if filter_val != '':
            result = PartnerUser.objects.filter(Q(auth_user_id__first_name__icontains=filter_val) | Q(auth_user_id__last_name__icontains=filter_val))
        else:
            result = PartnerUser.objects.all().order_by(order_by)

        return result

    def get_context_data(self, **kwargs):

        context = super(UserPartnerListView, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', '')
        context['orderby'] = self.request.GET.get('orderby', 'id')
        context['all_table_fields'] = PartnerUser._meta.get_fields()

        return context


class UserPartnerResumeCreateView(View):

    def get(self, request, *args, **kwargs):

        partner_user = PartnerUser.objects.get(id=self.kwargs['pk'])

        context = {
            "partner_user": partner_user,
        }

        return render(request, 'crm/admin_partner_resume_create.html', context)

    def post(self, request, *args, **kwargs):

        partner_instance = PartnerUser.objects.get(id=self.kwargs['pk'])

        # PartnerEducation
        pe_degree_type = request.POST.getlist('degree[]')
        pe_school_name = request.POST.getlist('school[]')
        pe_field_name = request.POST.getlist('field[]')
        pe_date_graduated = request.POST.getlist('graduated[]')
        pe_school_address = request.POST.getlist('school_address[]')

        # PartnerLicense
        pl_license_name = request.POST.getlist('license_name[]')
        pl_license_code = request.POST.getlist('license_code[]')
        pl_expiration_date = request.POST.getlist('license_expiration_date[]')
        pl_address_acquired = request.POST.getlist('license_address[]')
        pl_is_compact = request.POST.getlist('license_is_compact[]')

        # PartnerCertification
        pc_cert_name = request.POST.getlist('certification_name[]')
        pc_cert_code = request.POST.getlist('certification_code[]')
        pc_expiration_date = request.POST.getlist('certification_expiration_date[]')
        pc_address_acquired = request.POST.getlist('certification_address[]')

        # PartnerReference
        pr_name = request.POST.getlist('reference_name[]')
        pr_position = request.POST.getlist('reference_position[]')
        pr_phone_number = request.POST.getlist('reference_phone_number[]')
        pr_email = request.POST.getlist('reference_email[]')
        pr_office_name = request.POST.getlist('reference_office_name[]')
        pr_office_address = request.POST.getlist('reference_office_address[]')
        pr_start_date = request.POST.getlist('reference_start_date[]')
        pr_end_date = request.POST.getlist('reference_end_date[]')

        # PartnerSkill
        ps_skills = request.POST.get('skills')

        # PartnerCoverLetter
        cover_letter = request.POST.get('cover_letter')
        cover_l = "".join(cover_letter.splitlines())
        cover_l = cover_l.replace("\"", "\'")

        # PartnerProfessionalSummary
        professional_summary = request.POST.get('professional_summary')
        summary = "".join(professional_summary.splitlines())
        summary = summary.replace("\"", "\'")

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

        # Saving education
        i = 0
        for degree_type in pe_degree_type:
            education_obj = PartnerEducation(
                degree_type=degree_type,
                school_name=pe_school_name[i],
                field_name=pe_field_name[i],
                date_graduated=pe_date_graduated[i],
                school_address=pe_school_address[i],
                auth_user_id=partner_instance
            )
            education_obj.save()
            i += 1


        # Saving licenses
        j = 0
        for license_name in pl_license_name:
            license_obj = PartnerLicense(
                license_name=license_name,
                license_code=pl_license_code[j],
                expiration_date=pl_expiration_date[j],
                address_acquired=pl_address_acquired[j],
                is_compact=pl_is_compact[j],
                auth_user_id=partner_instance
            )
            license_obj.save()
            j += 1


        # Saving certifications
        k = 0
        for cert_name in pc_cert_name:
            cert_obj = PartnerCertification(
                cert_name=cert_name,
                cert_code=pc_cert_code[k],
                expiration_date=pc_expiration_date[k],
                address_acquired=pc_address_acquired[k],
                auth_user_id=partner_instance
            )
            cert_obj.save()
            k += 1
        

        # Saving references
        l = 0
        for reference in pr_name:
            reference_obj = PartnerReference(
                name=reference,
                position=pr_position[l],
                phone_number=pr_phone_number[l],
                email=pr_email[l],
                office_name=pr_office_name[l],
                office_address=pr_office_address[l],
                start_date=pr_start_date[l],
                end_date=pr_end_date[l],
                auth_user_id=partner_instance
            )
            reference_obj.save()
            l += 1

        # Saving skills
        skill_list = ps_skills.split(',')
        for skill in skill_list:
            skill_obj = PartnerSkill(skill_name=skill, auth_user_id=partner_instance)
            skill_obj.save()


        #Saving cover letter
        cover_letter_obj = PartnerCoverLetter(letter=cover_l, auth_user_id=partner_instance)
        cover_letter_obj.save()

        #Saving professional summary
        professional_summary_obj = PartnerProfessionalSummary(summary=summary, auth_user_id=partner_instance)
        professional_summary_obj.save()

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
                auth_user_id=partner_instance,
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
                auth_user_id=partner_instance,
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
                auth_user_id=partner_instance,
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
                auth_user_id=partner_instance,
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
                auth_user_id=partner_instance,
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
            auth_user_id=partner_instance,
            )
            work_history_3_obj.save()

        partner_instance.progress_mark = 80
        partner_instance.save()

        return HttpResponse("Saved")


class UserPartnerResumeUpdateView(View):
    def get(self, request, *args, **kwargs):

        partner_user = PartnerUser.objects.get(id=self.kwargs['pk'])
        p_education = PartnerEducation.objects.filter(auth_user_id=partner_user.id)
        p_license = PartnerLicense.objects.filter(auth_user_id=partner_user.id)
        p_certification = PartnerCertification.objects.filter(auth_user_id=partner_user.id)
        p_reference = PartnerReference.objects.filter(auth_user_id=partner_user.id)
        p_skill = PartnerSkill.objects.filter(auth_user_id=partner_user.id)
        p_cover = PartnerCoverLetter.objects.get(auth_user_id=partner_user.id)
        p_summary = PartnerProfessionalSummary.objects.get(auth_user_id=partner_user.id)
        p_work = PartnerWorkHistory.objects.filter(auth_user_id=partner_user.id)

        context = {
            "partner_user": partner_user,
            "p_education": p_education,
            "p_license": p_license,
            "p_certification": p_certification,
            "p_reference": p_reference,
            "p_skill": p_skill,
            "p_cover": p_cover,
            "p_summary": p_summary,
            "p_work": p_work,
        }

        return render(request, 'crm/admin_partner_resume_update.html', context)

    def post(self, request, *args, **kwargs):

        partner_instance = PartnerUser.objects.get(id=self.kwargs['pk'])

        # PartnerEducation

        pe_ids = request.POST.getlist('education_id[]')
        pe_degree_type = request.POST.getlist('degree[]')
        pe_school_name = request.POST.getlist('school[]')
        pe_field_name = request.POST.getlist('field[]')
        pe_date_graduated = request.POST.getlist('graduated[]')
        pe_school_address = request.POST.getlist('school_address[]')

        # PartnerLicense
        pl_ids = request.POST.getlist('license_id[]')
        pl_license_name = request.POST.getlist('license_name[]')
        pl_license_code = request.POST.getlist('license_code[]')
        pl_expiration_date = request.POST.getlist('license_expiration_date[]')
        pl_address_acquired = request.POST.getlist('license_address[]')
        pl_is_compact = request.POST.getlist('license_is_compact[]')

        # PartnerCertification
        pc_ids = request.POST.getlist('certification_id[]')
        pc_cert_name = request.POST.getlist('certification_name[]')
        pc_cert_code = request.POST.getlist('certification_code[]')
        pc_expiration_date = request.POST.getlist('certification_expiration_date[]')
        pc_address_acquired = request.POST.getlist('certification_address[]')
        pc_file = request.FILES.getlist('certification_file[]')

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

        # PartnerSkill
        ps_skills = request.POST.get('skills')

        # PartnerCoverLetter
        cover_letter = request.POST.get('cover_letter')
        cover_l = "".join(cover_letter.splitlines())
        cover_l = cover_l.replace("\"", "\'")

        # PartnerProfessionalSummary
        professional_summary = request.POST.get('professional_summary')
        summary = "".join(professional_summary.splitlines())
        summary = summary.replace("\"", "\'")

        # PartnerWorkHistory - 1
        wd_id_1 = request.POST.get('wd_id_1', None)
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
        wd_id_2 = request.POST.get('wd_id_2', None)
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
        wd_id_3 = request.POST.get('wd_id_3', None)
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

        # Saving education
        i = 0
        for degree_type in pe_degree_type:
            pe_id = pe_ids[i]
            if pe_id == 'blank' and pe_school_name[i] != '':
                education_obj = PartnerEducation(
                    degree_type=degree_type,
                    school_name=pe_school_name[i],
                    field_name=pe_field_name[i],
                    date_graduated=pe_date_graduated[i],
                    school_address=pe_school_address[i],
                    auth_user_id=partner_instance
                )
                education_obj.save()
            else:
                if pe_school_name[i] != '':
                    education_obj = PartnerEducation.objects.get(id=pe_id)      
                    education_obj.degree_type = degree_type
                    education_obj.school_name = pe_school_name[i]
                    education_obj.field_name = pe_field_name[i]
                    education_obj.date_graduated = pe_date_graduated[i]
                    education_obj.school_address = pe_school_address[i]
                    education_obj.auth_user_id = partner_instance
                    education_obj.save()
                   
            i += 1


        # Saving licenses
        j = 0
        for license_name in pl_license_name:
            pl_id = pl_ids[j]
            if pl_id == 'blank':
                if license_name != '':
                    license_obj = PartnerLicense(
                        license_name=license_name,
                        license_code=pl_license_code[j],
                        expiration_date=pl_expiration_date[j],
                        address_acquired=pl_address_acquired[j],
                        is_compact=pl_is_compact[j],
                        auth_user_id=partner_instance
                    )
                    license_obj.save()
            else:
                if license_name != '' and pl_is_compact[j] != '':
                    license_obj = PartnerLicense.objects.get(id=pl_id)
                    license_obj.license_name=license_name
                    license_obj.license_code=pl_license_code[j]
                    license_obj.expiration_date=pl_expiration_date[j]
                    license_obj.address_acquired=pl_address_acquired[j]
                    license_obj.is_compact=pl_is_compact[j]
                    license_obj.auth_user_id=partner_instance
                    license_obj.save()
            j += 1


        # Saving certifications
        k = 0
        for cert_name in pc_cert_name:
            pc_id = pc_ids[k]
            if pc_id == 'blank':
                if cert_name != '':
                    cert_obj = PartnerCertification(
                        cert_name=cert_name,
                        cert_code=pc_cert_code[k],
                        expiration_date=pc_expiration_date[k],
                        address_acquired=pc_address_acquired[k],
                        auth_user_id=partner_instance
                    )
                    cert_obj.save()
            else:
                if cert_name != '':
                    cert_obj = PartnerCertification.objects.get(id=pc_id)
                    cert_obj.cert_name=cert_name
                    cert_obj.cert_code=pc_cert_code[k]
                    cert_obj.expiration_date=pc_expiration_date[k]
                    cert_obj.address_acquired=pc_address_acquired[k]
                    cert_obj.auth_user_id=partner_instance
                    cert_obj.save()
            k += 1
        

        # Saving references
        l = 0
        for reference in pr_name:
            pr_id = pr_ids[l]
            if pr_id == 'blank':
                if reference != '':
                    reference_obj = PartnerReference(
                        name=reference,
                        position=pr_position[l],
                        phone_number=pr_phone_number[l],
                        email=pr_email[l],
                        office_name=pr_office_name[l],
                        office_address=pr_office_address[l],
                        start_date=pr_start_date[l],
                        end_date=pr_end_date[l],
                        auth_user_id=partner_instance
                    )
                    reference_obj.save()
            else:
                if reference != '':
                    reference_obj = PartnerReference.objects.get(id=pr_id)
                    reference_obj.name=reference
                    reference_obj.position=pr_position[l]
                    reference_obj.phone_number=pr_phone_number[l]
                    reference_obj.email=pr_email[l]
                    reference_obj.office_name=pr_office_name[l]
                    reference_obj.office_address=pr_office_address[l]
                    reference_obj.start_date=pr_start_date[l]
                    reference_obj.end_date=pr_end_date[l]
                    reference_obj.auth_user_id=partner_instance
                    reference_obj.save()
            l += 1

        # Saving skills
        PartnerSkill.objects.filter(auth_user_id=partner_instance).delete()

        skill_list = ps_skills.split(',')
        for skill in skill_list:
            skill_obj = PartnerSkill(skill_name=skill, auth_user_id=partner_instance)
            skill_obj.save()

        #Saving cover letter        
        cover_letter_obj = PartnerCoverLetter.objects.get(auth_user_id=partner_instance)
        cover_letter_obj.letter = cover_l
        cover_letter_obj.save()

        #Saving professional summary
        professional_summary_obj = PartnerProfessionalSummary.objects.get(auth_user_id=partner_instance)
        professional_summary_obj.summary = summary
        professional_summary_obj.save()

        #Saving work history 1
        work_history_1_obj = PartnerWorkHistory.objects.get(id=wd_id_1)
        if work_designation_1 == None and work_phone_number_1 == None and work_email_1 == None:
            work_history_1_obj.designation=''
            work_history_1_obj.phone_number=''
            work_history_1_obj.email=''
            work_history_1_obj.office_name=''
            work_history_1_obj.office_address=''
            work_history_1_obj.start_date=''
            work_history_1_obj.end_date=''
            work_history_1_obj.responsibilities=''
            work_history_1_obj.auth_user_id=partner_instance
            work_history_1_obj.save()
        else:
            work_history_1_obj.designation=work_designation_1
            work_history_1_obj.phone_number=work_phone_number_1
            work_history_1_obj.email=work_email_1
            work_history_1_obj.office_name=work_office_name_1
            work_history_1_obj.office_address=work_office_address_1
            work_history_1_obj.start_date=work_start_date_1
            work_history_1_obj.end_date=work_end_date_1
            work_history_1_obj.responsibilities=work_r_1
            work_history_1_obj.auth_user_id=partner_instance
            work_history_1_obj.save()

        #Saving work history 2
        work_history_2_obj = PartnerWorkHistory.objects.get(id=wd_id_2)
        if work_designation_2 == None and work_phone_number_2 == None and work_email_2 == None:
            work_history_2_obj.designation=''
            work_history_2_obj.phone_number=''
            work_history_2_obj.email=''
            work_history_2_obj.office_name=''
            work_history_2_obj.office_address=''
            work_history_2_obj.start_date=''
            work_history_2_obj.end_date=''
            work_history_2_obj.responsibilities=''
            work_history_2_obj.auth_user_id=partner_instance
            work_history_2_obj.save()
        else:
            work_history_2_obj.designation=work_designation_2
            work_history_2_obj.phone_number=work_phone_number_2
            work_history_2_obj.email=work_email_2
            work_history_2_obj.office_name=work_office_name_2
            work_history_2_obj.office_address=work_office_address_2
            work_history_2_obj.start_date=work_start_date_2
            work_history_2_obj.end_date=work_end_date_2
            work_history_2_obj.responsibilities=work_r_2
            work_history_2_obj.auth_user_id=partner_instance
            work_history_2_obj.save()

        #Saving work history 3
        work_history_3_obj = PartnerWorkHistory.objects.get(id=wd_id_3)
        if work_designation_3 == None and work_phone_number_3 == None and work_email_3 == None:
            work_history_3_obj.designation=''
            work_history_3_obj.phone_number=''
            work_history_3_obj.email=''
            work_history_3_obj.office_name=''
            work_history_3_obj.office_address=''
            work_history_3_obj.start_date=''
            work_history_3_obj.end_date=''
            work_history_3_obj.responsibilities=''
            work_history_3_obj.auth_user_id=partner_instance
            work_history_3_obj.save()
        else:
            work_history_3_obj.designation=work_designation_3
            work_history_3_obj.phone_number=work_phone_number_3
            work_history_3_obj.email=work_email_3
            work_history_3_obj.office_name=work_office_name_3
            work_history_3_obj.office_address=work_office_address_3
            work_history_3_obj.start_date=work_start_date_3
            work_history_3_obj.end_date=work_end_date_3
            work_history_3_obj.responsibilities=work_r_3
            work_history_3_obj.auth_user_id=partner_instance
            work_history_3_obj.save()

        return HttpResponse("Saved")


class UserPartnerWithResumeListView(ListView):

    model = CustomUser
    fields = '__all__'
    template_name = 'crm/admin_partner_with_resume_list.html'

    # Number of partners to paginate
    paginate_by = 10

    def get_queryset(self):

        filter_val = self.request.GET.get('filter', '')
        order_by = self.request.GET.get('orderby', 'id')

        if filter_val != '':
            result = PartnerUser.objects.filter(Q(auth_user_id__first_name__icontains=filter_val) | Q(auth_user_id__last_name__icontains=filter_val) | Q(id__icontains=filter_val))
        else:
            result = PartnerUser.objects.all().order_by(order_by)

        return result

    def get_context_data(self, **kwargs):

        context = super(UserPartnerWithResumeListView, self).get_context_data(**kwargs)
        partner_id = self.request.GET.get('partner_id', None)
        if partner_id:
            context['partner_user'] = PartnerUser.objects.get(id=partner_id)
            context['partner_education'] = PartnerEducation.objects.filter(auth_user_id=partner_id)
            context['partner_licenses'] = PartnerLicense.objects.filter(auth_user_id=partner_id)
            context['partner_certifications'] = PartnerCertification.objects.filter(auth_user_id=partner_id)
            context['partner_references'] = PartnerReference.objects.filter(auth_user_id=partner_id)
            context['partner_skills'] = PartnerSkill.objects.filter(auth_user_id=partner_id)
            context['partner_cover'] = PartnerCoverLetter.objects.get(auth_user_id=partner_id)
            context['partner_summary'] = PartnerProfessionalSummary.objects.get(auth_user_id=partner_id)
            context['partner_works'] = PartnerWorkHistory.objects.filter(auth_user_id=partner_id)

        page_number = self.request.GET.get('page', None)
        context['current_id'] = partner_id
        if page_number:
            context['page_number'] = page_number
        context['filter'] = self.request.GET.get('filter', '')
        context['orderby'] = self.request.GET.get('orderby', 'id')
        context['all_table_fields'] = PartnerUser._meta.get_fields()
        
        

        return context


class UserPartnerMediaUpload(View):

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

        partner_user = PartnerUser.objects.get(id=self.kwargs['pk'])
        partner_education_media = PartnerEducationMedia.objects.filter(auth_user_id=partner_user)
        partner_lc_media = PartnerLCMedia.objects.filter(auth_user_id=partner_user)
        partner_other_media = PartnerOtherMedia.objects.filter(auth_user_id=partner_user)

        context = {
            "partner_user": partner_user,
            "partner_education_media": partner_education_media,
            "partner_lc_media": partner_lc_media,
            "partner_other_media": partner_other_media
        }

        return render(request, 'crm/admin_partner_media_upload.html', context)