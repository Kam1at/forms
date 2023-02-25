from django.contrib.auth.forms import UserChangeForm, PasswordResetForm
from django import forms

from Users.models import User


class CustomEditUserForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'avatar')


class NewCustomEditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class CustomPasswordResetForm(PasswordResetForm):
    pass
