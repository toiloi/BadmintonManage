from django import forms
from BCourt.models import Court, Address, CourtTimeSlot, San

class CourtForm(forms.ModelForm):
    class Meta:
        model = Court
        fields = ['maCourt', 'name', 'price', 'description', 'img']  # Xóa 'address' và 'courtManager'
    
    def __init__(self, *args, **kwargs):
        super(CourtForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control form-control-lg',
                'style': 'height: 50px;'
            })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'rows': 4
        })

class SanForm(forms.ModelForm):
    class Meta:
        model = San
        fields = ['maSan', 'numSan']
    
    def __init__(self, *args, **kwargs):
        super(SanForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control form-control-lg',
                'style': 'height: 50px;'
            })

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['soNha', 'duong', 'phuong', 'quan', 'tinh']
    
    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control form-control-lg',
                'style': 'height: 50px;'
            })


class CourtTimeSlotForm(forms.ModelForm):
    class Meta:
        model = CourtTimeSlot
        fields = ['court', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }
