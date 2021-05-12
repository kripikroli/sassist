from datetime import date

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.views import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, View

from profiles.models import CustomUser, PartnerUser

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


class UserPartnerListView(ListView):

    model = CustomUser
    fields = '__all__'
    template_name = 'crm/admin_partner_list.html'

    # Number of partners to paginate
    paginate_by = 1

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