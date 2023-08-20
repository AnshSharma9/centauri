from django.shortcuts import render, redirect
from django.db import connection
from .forms import ContactForm
import smtplib
from email.mime.text import MIMEText
from django.conf import settings
from .models import Contact
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')



def gallery(request):
    gallery_images = [
        {'url': 'images/school.jpg'},
        {'url': 'images/weblogo.jpg'},

    ]
    context = {'gallery_images': gallery_images}
    return render(request, 'gallery.html', context)


def contact(request):
    if request.method == "POST":
        # Process the form data

        name = request.POST["name"]
        surname = request.POST["surname"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        query = request.POST["query"]

        # Send an email
        subject = 'Contact Form Submission'
        message = f"Name: {name}\nSurname: {surname}\nEmail: {email}\nPhone: {phone}\nQuery: {query}"
        from_email = settings.EMAIL_HOST_USER  
        recipient = settings.EMAIL_RECIPIENT

        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = ', '.join(recipient)

        smtp = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        smtp.sendmail(from_email, recipient, msg.as_string())
        smtp.quit()

        success_message = "Form submitted successfully"
        return render(request, "contact.html", {"success_message": success_message})

    return render(request, "contact.html")
