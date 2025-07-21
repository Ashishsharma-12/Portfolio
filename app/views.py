from django.shortcuts import render, redirect
import requests
from django.contrib import messages
from .models import *
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .forms import ContactForm

# Create your views here.

def homepage(request):
    
    skills = Skills_Library.objects.all()
    projects = Projects.objects.all()
    edu = Education.objects.all()
    work = Work_Experience.objects.all().order_by('-end_year', '-start_year')
    cert = Certifications.objects.all()
    form = ContactForm()

    context = {
                'skills' : skills, 'projects': projects, 'edu': edu, 'work': work, 'cert': cert, 
                'len_prj': len(projects), 'len_cert': len(cert), 'form': form
               }

    return render(request,'index.html', context=context)

def contact(request):
    if request.method =="POST":
        # data = json.loads(request.body)
        fname  = request.POST.get('name')
        femail = request.POST.get('email')
        fsub = request.POST.get('subject')
        fmsg = request.POST.get('message')

        if fname and femail and fsub and fmsg:

            query = Contact(name = fname, email= femail, subject= fsub, msg= fmsg)
            query.save()
            try:
                send_mail(
                    "Contact Form Submission",
                    f"Name: {fname}\nEmail: {femail}\nSubject: {fsub}\nMessage: {fmsg}",
                    femail,  # Replace with your email
                    ['ashishrsharma99@gmail.com'],  # Replace with recipient email(s)
                    fail_silently=False,
                )
                return messages.success(request, "Thanks for contacting. I will get back to you as soon as possible.")
            
            except(Exception):
                print(Exception.with_traceback)
                return messages.error(request, "Something went wrong. Please try again later.")
        else:
            return messages.danger(request, "Missing required fields.")

    skills = Skills_Library.objects.all()
    projects = Projects.objects.all()
    edu = Education.objects.all()
    work = Work_Experience.objects.all().order_by('-end_year', '-start_year')
    cert = Certifications.objects.all()
    form = ContactForm()
    
    context = {
                'skills' : skills, 'projects': projects, 'edu': edu, 'work': work, 'cert': cert, 
                'len_prj': len(projects), 'len_cert': len(cert),'form': form
               }

    return redirect(request,'index.html', context=context)


def rock_paper_sciscor(request):
    
    return render(request,'rock-paper-sciscor.html')
