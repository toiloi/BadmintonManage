from django import forms
from .models import Voucher


class Gangzbit(forms.ModelForm):
    class Meta:
        model = Voucher
        fields = ['voucher','court','percent']
        widgets = {
            'voucher': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập mã khuyến mãi'}),
            'court': forms.Select(attrs={'class': 'form-control'}),
            'percent': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nhập phần trăm giảm giá', 'min': 0, 'max': 40}),
        }
        