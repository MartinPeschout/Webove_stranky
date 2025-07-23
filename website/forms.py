# website/forms.py
from django import forms

class PoptavkaForm(forms.Form):
    jmeno = forms.CharField(label="Jméno a příjmení", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="E-mail", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    telefon = forms.CharField(label="Telefon", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    odkud = forms.CharField(label="Odkud (místo nakládky)", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    kam = forms.CharField(label="Kam (místo vykládky)", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    zbozi = forms.CharField(label="Druh zboží", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    datum = forms.DateField(label="Požadované datum", widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    poznamka = forms.CharField(label="Další poznámka", widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
