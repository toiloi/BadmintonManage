from django import forms
from .models import VeDatSan, TimeSlot, Flag

class VeDatSanForm(forms.ModelForm):
    class Meta:
        model = VeDatSan
        fields = ['customer', 'tongTien', 'checkin', 'voucher', 'flag']

class FlagForm(forms.ModelForm):
    class Meta:
        model = Flag
        fields = ['san', 'timeslot', 'date']
