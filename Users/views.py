import datetime
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView
from Users.forms import CustomEditUserForm, NewCustomEditUserForm, CustomPasswordResetForm
from Users.models import User
from config import settings


class CustomLoginView(LoginView):
    template_name = 'users/login.html'


class UserCreateProfileView(CreateView):
    model = User
    form_class = NewCustomEditUserForm
    template_name = 'users/user_create.html'
    success_url = '/'

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            ###
            self.object.token = make_password(self.object.password).replace('/', '')
            self.object.token_created = datetime.datetime.now().astimezone()
            self.object.is_active = False
            ###
            self.object.set_password(form.data.get('password'))
            self.object.save()
            ###
            send_mail(
                subject='Активация',
                message=f'http://localhost:8000/users/activate/{self.object.token}/',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[self.object.email],

            )
        return super().form_valid(form)


class UserEditProfileView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = CustomEditUserForm
    success_url = reverse_lazy('prod:product')

    def get_object(self, queryset=None):
        return self.request.user


class MyPasswordChangeView(PasswordChangeView):
    success_url = '/'
    template_name = 'users/change_passwd.html'


def user_activation(request, token):
    u = User.objects.filter(token=token).first()
    if u:
        u.is_active = True
        u.save()
    return redirect('http://localhost:8000')


class CustomPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset_form.html'
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('password_reset_confirm')
    email_template_name = 'users/email_reset.html'
    from_email = settings.EMAIL_HOST_USER
