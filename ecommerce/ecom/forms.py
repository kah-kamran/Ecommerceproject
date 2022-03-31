from django import forms  
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model

from ecom.models import Contact, User, Product
from django.db import models
from django.forms import fields, widgets
from django.utils.translation import gettext, gettext_lazy as _


CHOICES = (
   ('S', 'Seller'),
   ('B', 'Buyer')
)

class UserForm(forms.ModelForm):
    customer = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=CHOICES,
    )
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['name',  'mobile', 'email', 'username', 'password',  'country', 'customer', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),

            'email': forms.EmailInput(attrs={'class':'form-control'}),
            # 'mobile': forms.CharField(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
            'password2': forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
            'mobile':forms.TextInput(attrs={'class': 'form-control'}),

            # 'customer' : forms.CharField(attrs={'class':'form-control'}),
            # 'country' : forms.CharField(attrs={'class':'form-control'}),
            'address' : forms.Textarea(attrs={'class':'form-control'}),

            

            # 'customer' : forms.MultipleChoiceField(forms.CheckboxSelectMultiple, choices=CHOICES) 
            
        }
        labels = {
            'password' : 'Password',
            'password2': 'Confirm Password',
            'mobile': 'Mobile No'
        }
        # exclude = ['name']



class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}))

    

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'product_image', 'price', 'description']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
