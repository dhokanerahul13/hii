from attr import fields
from django import forms
from stu.models import movie


class movieform(forms.ModelForm):
    class Meta:
        model=movie
        fields='__all__'