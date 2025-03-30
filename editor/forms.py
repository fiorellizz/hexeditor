from django import forms
from .models import ArquivoBinario

class UploadForm(forms.ModelForm):
    class Meta:
        model = ArquivoBinario
        fields = ["nome", "arquivo"]
