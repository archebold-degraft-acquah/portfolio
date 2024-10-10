from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


class ReplyMessageForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['subject', 'message']
