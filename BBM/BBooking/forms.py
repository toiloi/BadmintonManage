from django import forms
from .models import VeDatSan, TimeSlot, Flag, Voucher

class VeDatSanForm(forms.ModelForm):
    class Meta:
        model = VeDatSan
        fields = ['customer', 'tongTien', 'checkin', 'voucher', 'flag', 'type']

class FlagForm(forms.ModelForm):
    class Meta:
        model = Flag
        fields = ['san', 'timeslot', 'date']
