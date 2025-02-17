from django import forms
from .models import Court

class CourtForm(forms.ModelForm):
    class Meta:
        model = Court
        fields = ['name', 'address', 'phone', 'price']
