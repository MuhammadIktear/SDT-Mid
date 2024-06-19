from django import forms
from .models import Car, Brand,Comment

class CarForm(forms.ModelForm):
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), widget=forms.Select())

    class Meta:
        model = Car
        fields = ['image', 'name', 'description', 'quantity', 'price', 'brand']

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['name', 'email', 'body']
