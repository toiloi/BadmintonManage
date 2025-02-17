from django import forms
from BCourt.models import Court, Sonha, Duong, Phuong, Quan, Tinh

class CourtForm(forms.ModelForm):
    class Meta:
        model = Court
        fields = ['courtManager', 'maCourt', 'name', 'price', 'description', 'img']

class AddressForm(forms.Form):
    sonha = forms.ModelChoiceField(queryset=Sonha.objects.all(), required=True, label="Số Nhà")
    duong = forms.ModelChoiceField(queryset=Duong.objects.all(), required=True, label="Đường")
    phuong = forms.ModelChoiceField(queryset=Phuong.objects.all(), required=True, label="Phường")
    quan = forms.ModelChoiceField(queryset=Quan.objects.all(), required=True, label="Quận")
    tinh = forms.ModelChoiceField(queryset=Tinh.objects.all(), required=True, label="Tỉnh/Thành phố")