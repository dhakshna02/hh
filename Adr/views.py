
from venv import logger
from django.shortcuts import render
from django .http import HttpResponse
from numpy import fix
from .forms import  job,cont
from django.urls import reverse
from django.shortcuts import redirect
from .models import jobpost, contact, masterdatamanagement,bigdata,itesglobal
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from smtplib import SMTPException
from django.core.mail import EmailMultiAlternatives







def home(response):
 return render(response,"Adr/home.html",{} ) 
# Create your views here.

#def v1(response , id):
 return HttpResponse(f"The index is ID { id}") 


def About(request):
 return render(request,"Adr/about.html",{})


def products(request):
 return render(request,"Adr/products.html",{})


def services(request):
 return render(request,"Adr/services.html",{})

def fotopia(request):
 return render(request,"Adr/fotopia.html",{})

def smartboat(request):
 return render(request,"Adr/smartboat.html",{})

def erp(request):
 return render(request,"Adr/erp.html",{})

def itstaffing(request):
 return render(request,"Adr/itstaffing.html",{})


def sap(response):
 return render(response,"Adr/sap.html",{} )


def s4hana(response):
 return render(response,"Adr/s4hana.html",{} )


def successfactors(response):
 return render(response,"Adr/successfactors.html",{} )   


def sapb1(response):
 return render(response,"Adr/sapb1.html",{} ) 


def hybris(response):
 return render(response,"Adr/hybris.html",{} ) 


def manufacturing(response):
 return render(response,"Adr/manufacturing.html",{} ) 


def automotive(response):
 return render(response,"Adr/automotive.html",{} ) 


def logistics(response):
 return render(response,"Adr/logistics.html",{} )


def retail(response):
 return render(response,"Adr/retail.html",{} )


def education(response):
 return render(response,"Adr/education.html",{} )


def career(request):
 titles= "jobopening"
 posts = jobpost.objects.all()
 
 return render(request,"Adr/career.html",{'titles':titles,'posts':posts} )

def jobforms(request):
    form =job()
    if request.method == 'POST':
      print(request.FILES),
      to = request.POST.get('email')
      te = request.FILES.get('resume')
      print(te)
      print(to)
      form =job(request.POST,files=request.FILES)
      if form.is_valid():
        form.save()
         
        email = EmailMessage(
                'Document Uploaded',
                f'Your document has been uploaded successfully.\n\n your resume uploaded was {te}',
                'dhakshnamoorthydhandauthapani@gmail.com',
                [to,'dhakshna021204@gmail.com']
            )
       
        email.send()  
        return redirect('careersucess') 
      else:
       print( form.errors) 
       return redirect('careerfail')
 
    return render (request,'Adr/jobforms.html',{})


def contact(request):
 form =cont()
 if request.method == 'POST':
   print(request.POST)
   to = request.POST.get('email')
   print(to)
   thr = request.POST.get('name')
   vr = request.POST.get('mesg')
   print(vr)
   print(thr)
   form =cont(request.POST)
   if form.is_valid():
       form.save()
       mesg = EmailMessage(
       "Got Your Message – We’ll Be in Touch Soon!",
       f"Hi  {thr},\n\nThank you for contacting ADR Group. We’ve received your query and our support team is already on it! You can expect a response from us shortly.\n\n We’re always here for you!\n\n Your query:{vr}\n\n\n\n Thanks & Regards\n Support Team\n AnDnR Soft Solutions Pvt. Ltd.\n Phone:  +91 44 48545680\n E-mail: info@adrgrp.com",

       "dhakshnamoorthydhandauthapani@gmail.com",
       [to,"dhakshna021204@gmail.com"]   ,  
         
                  
       )
       mesg.send()
       return redirect('contactsucess') 
   else:
       print( form.errors) 
       return redirect('contactfail')
 return render(request,'Adr/contact.html',{} )


def masterdata(request):
 titles= "masterdatamanagement"
 posts = masterdatamanagement.objects.all()
 print(masterdatamanagement.objects.all())
 
 return render(request,"Adr/masterdatamanagement.html",{'titles':titles,'posts':posts} )


def bigdat(request):
 titles= "bigdata"
 posts = bigdata.objects.all()
 
 return render(request,"Adr/bigdata.html",{'titles':titles,'posts':posts} )


def itesandglobalsupport(request):
 titles= "ites and global support"
 posts = itesglobal.objects.all()
 
 return render(request,"Adr/itesandglobalsupport.html",{'titles':titles,'posts':posts} )


def careersuccess(response):
 return render(response,"Adr/careersucess.html",{} ) 

def careerfail(response):
 return render(response,"Adr/careerfail.html",{} ) 

def contactsucess(response):
 return render(response,"Adr/contactsucess.html",{} ) 

def contactfail(response):
 return render(response,"Adr/contactfail.html",{} ) 