
from django import forms

class UploadFileForm(forms.Form):
    uploadfile = forms.FileField()
