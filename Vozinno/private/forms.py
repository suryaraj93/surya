from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from private.models import Email,Details
from django import forms

class CreateEmailForm(ModelForm):
    class Meta:
        model=Email
        fields="__all__"
        widgets={
            'mail':forms.TextInput(attrs={'class': 'form-control'})
        }


class CreateDetailsForm(ModelForm):
    class Meta:
        model=Details
        fields = "__all__"
        widgets = {'password': forms.PasswordInput(attrs={'class':'form-control'}),
                    'name' : forms.TextInput(attrs={'class': 'form-control'}),
                      # 'dob' :forms.DateField(attrs={'class': 'form-control'}),
                    'last_degree': forms.TextInput(attrs={'class': 'form-control'})
        }



class RegisterationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1']