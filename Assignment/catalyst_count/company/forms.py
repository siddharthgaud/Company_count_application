from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

""" class UploadFileForm(forms.Form):
    file = forms.FileField() """

class UploadFileForm(forms.Form):
    file = forms.FileField()

    def clean_file(self):
        file = self.cleaned_data['file']
        if file.size > 10485760:  # Limit file size to 10MB (10 * 1024 * 1024 bytes)
            raise forms.ValidationError("The uploaded file is too large. Maximum size allowed is 10MB.")
        return file

class FilterForm(forms.Form):
    name = forms.CharField(required=False, max_length=255)
    industry = forms.CharField(required=False, max_length=255)
    country = forms.CharField(required=False, max_length=255)



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
