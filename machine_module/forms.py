from django.forms import ModelForm
from machine_module.models import dataInput

class dataInput_form(ModelForm):
    class Meta:
        model = dataInput
        fields = '__all__'
