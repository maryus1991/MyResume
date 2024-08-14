from django import forms
from django.forms.models import ModelForm

from .models import ContactUser


class Contactus_form(ModelForm):
    class Meta:
        model = ContactUser
        fields = ['first_name', 'last_name', 'email', 'message']
        widgets = {
            'Profile': forms.HiddenInput(attrs={
                'type': 'hidden',
                'value': 'user',
            }),
            'skill': forms.HiddenInput(attrs={
                'type': 'hidden',
                'value': 'user',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'contact-name form-control',
                'id': 'name',
                'placeholder': "First Name"
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'contact-email form-control',
                'id': 'L_name',
                'placeholder': "Last Name"
            }),
            'email': forms.TextInput(attrs={
                'class': 'contact-subject form-control',
                'id': 'email',
                'placeholder': "Your Email"
            }),
            'message': forms.Textarea(attrs={
                'class': "contact-message",
                'id': "message",
                'name': "message",
                'rows': "6",
                'placeholder': "Your Message",
            })
        }
