# website/forms.py
from django import forms

class PoptavkaForm(forms.Form):
    jmeno = forms.CharField(label="Jméno a příjmení", max_length=100)
    email = forms.EmailField(label="E-mail")
    telefon = forms.CharField(label="Telefon", max_length=30)
    odkud = forms.CharField(label="Odkud (místo nakládky)", max_length=100)
    kam = forms.CharField(label="Kam (místo vykládky)", max_length=100)
    zbozi = forms.CharField(label="Druh zboží", max_length=100)
    datum = forms.DateField(label="Požadované datum", widget=forms.DateInput(attrs={'type': 'date'}))
    poznamka = forms.CharField(label="Další poznámka", widget=forms.Textarea, required=False)
