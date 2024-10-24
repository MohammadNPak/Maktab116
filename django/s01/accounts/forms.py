from django import forms
from django.forms import ValidationError
from .models import User


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=40)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    
    @staticmethod
    def my_password_validation(password):
        if len(password)<5:
            raise ValidationError("password length must be grater than 4!")

    def clean_password1(self):
        password1 = self.cleaned_data["password1"]
        self.my_password_validation(password1)
        return password1

    def clean_password2(self):
        password2 = self.cleaned_data["password2"]
        self.my_password_validation(password2)
        return password2
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1!=password2:
            raise ValidationError("password1 must be equal to password2")
        



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("picture",)