from unicodedata import name
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from formapp.models import UploadForm

# Create class to define the form fields
class StudentForm(forms.Form):
    name = forms.CharField(label="Enter name", max_length=40)
    error_messages = {
                 'required':"Please Enter Correct Name"
                 }
    def clean_name(self):
        data = self.cleaned_data['name']
        if "Tannu Yadav" != data:
            raise ValidationError("Error")
        return data

class FormUpload(forms.ModelForm):  
    class Meta:  
        model = UploadForm  
        fields = "__all__"