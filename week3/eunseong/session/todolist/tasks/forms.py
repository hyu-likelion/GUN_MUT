from django import forms
from django.forms import ModelForm
from .models import *

class TaskForm(forms.ModelForm):
    title = forms.CharField(
    	widget= forms.TextInput(
            attrs={'placeholder': '할 일을 입력하세요', 'class':'form-control'}
        )
    )

    class Meta:
        model = Task
        fields = '__all__'