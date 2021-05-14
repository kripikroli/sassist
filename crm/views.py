from datetime import date
from django.contrib import auth

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.views import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q, fields
from django.http import HttpResponse, HttpResponseRedirect
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
)

def admin_dashboard_view(request):
    return render(request, 'crm/admin_dashboard.html')

def login_view(request):
    error_message = None
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('crm:admin_dashboard_view')

        else:
            error_message = 'Oppsss... something went wrong'

    context = {
        'form': form,
        'error_message': error_message
    }
    return render(request, 'auth/login.html', context)


def logout_view(request):

    logout(request)
    return redirect('crm:login_view')


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

        print(partneruser.profile_pic)

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
    paginate_by = 4

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
        pe_file = request.FILES.getlist('educ_file[]')

        # PartnerLicense
        pl_license_name = request.POST.getlist('license_name[]')
        pl_license_code = request.POST.getlist('license_code[]')
        pl_expiration_date = request.POST.getlist('license_expiration_date[]')
        pl_address_acquired = request.POST.getlist('license_address[]')
        pl_file = request.FILES.getlist('license_file[]')
        pl_is_compact = request.POST.getlist('license_is_compact[]')

        # PartnerCertification
        pc_cert_name = request.POST.getlist('certification_name[]')
        pc_cert_code = request.POST.getlist('certification_code[]')
        pc_expiration_date = request.POST.getlist('certification_expiration_date[]')
        pc_address_acquired = request.POST.getlist('certification_address[]')
        pc_file = request.FILES.getlist('certification_file[]')

        # PartnerReference
        pr_name = request.POST.getlist('reference_name[]')
        pr_position = request.POST.getlist('reference_position[]')
        pr_phone_number = request.POST.getlist('reference_phone_number[]')
        pr_email = request.POST.getlist('reference_email[]')
        pr_office_name = request.POST.getlist('reference_office_name[]')
        pr_office_address = request.POST.getlist('reference_office_address[]')
        pr_file = request.FILES.getlist('reference_file[]')
        pr_start_date = request.POST.getlist('reference_start_date[]')
        pr_end_date = request.POST.getlist('reference_end_date[]')

        # PartnerSkill
        ps_skills = request.POST.get('skills')

        # PartnerCoverLetter
        cover_letter = request.POST.get('cover_letter')

        # Saving education
        i = 0
        for degree_type in pe_degree_type:
            education_obj = PartnerEducation(
                degree_type=degree_type,
                school_name=pe_school_name[i],
                field_name=pe_field_name[i],
                date_graduated=pe_date_graduated[i],
                school_address=pe_school_address[i],
                file=pe_file[i],
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
                file=pe_file[j],
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
                file=pc_file[k],
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
                file=pr_file[l],
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
        cover_letter_obj = PartnerCoverLetter(letter=cover_letter, auth_user_id=partner_instance)
        cover_letter_obj.save()

        return HttpResponse("Saved")
