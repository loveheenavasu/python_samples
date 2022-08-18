from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Product
class Signupform(UserCreationForm):
    first_name = forms.CharField(max_length=10)
    last_name = forms.CharField(max_length=10)
    email = forms.EmailField()
    password1 = forms.CharField(label='Enter password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput)
    class Meta(UserCreationForm):
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

    def clean_email(self):
      email=self.cleaned_data['email']
      if User.objects.filter(email= email).exists():
        raise forms.ValidationError("Email already exists")
      return email

class ProForm(forms.ModelForm):
  class Meta:
    model=Product
    fields="__all__"
    widgets={
      'name':forms.TextInput(attrs={'class':'form-control'}),
      'number_of_products':forms.TextInput(attrs={'class':'form-control'})
    }
