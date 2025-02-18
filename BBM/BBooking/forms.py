from django import forms
from .models import VeDatSan

class VeDatSanForm(forms.ModelForm):
    class Meta:
        model = VeDatSan
        fields = ['date', 'timeslot', 'customer', 'tongTien', 'checkin', 'voucher']