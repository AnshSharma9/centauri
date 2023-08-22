from django.shortcuts import render, redirect
from django.db import connection
from .forms import ContactForm
import smtplib
from email.mime.text import MIMEText
from django.conf import settings
from .models import Contact
from django.contrib.auth import authenticate, login
import smtplib, ssl
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
        from_email = settings.MAIL_FROM  
        recipient = settings.MAIL_RECIPIENT


        from email.message import EmailMessage
        msg = EmailMessage()
        msg['Subject'] = "NEW QUERY"
        msg['From'] = from_email
        msg['To'] = recipient
        msg.set_content(message)
        try:
            if settings.EMAIL_PORT == 465:
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT, context=context) as server:
                    server.connect(settings.EMAIL_HOST, settings.EMAIL_PORT)
                    server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                server.send_message(msg)
            elif settings.EMAIL_PORT == 587:
                with smtplib.SMTP(settings.EMAIL_HOST,settings.EMAIL_PORT ) as server:
                    server.connect(settings.EMAIL_HOST, settings.EMAIL_PORT)
                    server.starttls()

                    server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                    server.send_message(msg)
            else:
                print ("use 465 / 587 as port value")
                exit()
            success_message = "Form submitted successfully"
            return render(request, "contact.html", {"success_message": success_message})

        except Exception as e:
            print (e)        



    return render(request, "contact.html")
