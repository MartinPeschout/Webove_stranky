# website/views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import PoptavkaForm

def index(request):
    return render(request, 'website/index.html')

def poptat_dopravu(request):
    if request.method == 'POST':
        form = PoptavkaForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # složení textu mailu
            subject = f"Nová poptávka dopravy od {cd['jmeno']}"
            message = (
                f"Jméno: {cd['jmeno']}\n"
                f"E-mail: {cd['email']}\n"
                f"Telefon: {cd['telefon']}\n\n"
                f"Odkud: {cd['odkud']}\n"
                f"Kam: {cd['kam']}\n"
                f"Zboží: {cd['zbozi']}\n"
                f"Datum: {cd['datum']}\n\n"
                f"Poznámka:\n{cd['poznamka']}"
            )
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [settings.DISPECER_EMAIL],
                fail_silently=False,
            )
            return render(request, 'website/poptat_done.html', {'jmeno': cd['jmeno']})
    else:
        form = PoptavkaForm()
    return render(request, 'website/poptat.html', {'form': form})

def o_nas(request):
    return render(request, 'website/o_nas.html')
