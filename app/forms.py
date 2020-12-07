from django import forms

import datetime
from .models import User
from django.contrib.auth.forms import UserCreationForm

from django.core.exceptions import ValidationError


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'date_of_birth']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={
                'placeholder': 'MM/DD/YYYY'
            }),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = "Name"
        self.fields['username'].label = "Alias"

    def clean_date_of_birth(self):
        dob = self.cleaned_data['date_of_birth']
        today = datetime.date.today()
        if (dob.year + 16, dob.month, dob.day) > (today.year, today.month, today.day):
            raise forms.ValidationError(
                'Must be at least 16 years old to register')
        return dob


class Form(forms.Form):
    pass
