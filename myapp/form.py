from django import forms
from .models import DataPoint

class DataPointForm(forms.ModelForm):
    class Meta:
        model = DataPoint
        fields = ['name', 'size', 'compression_type']
