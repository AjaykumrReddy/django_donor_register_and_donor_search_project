from django import forms
from .models import Donor, Gender


class DonorsForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=Gender, widget=forms.RadioSelect, initial='M')

    class Meta:
        model = Donor
        fields = '__all__'
