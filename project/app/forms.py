from django import forms
from .models import Card

class ItemInfoForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['title', 'rs', 'des', 'image']