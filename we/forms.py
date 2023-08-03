from django import forms
from .models import *

class Instagram(forms.ModelForm):
    class Meta:
        model = Instagram
        fields = "__all__"


class Facebook(forms.ModelForm):
    class Meta:
        model = Facebook
        fields = "__all__"