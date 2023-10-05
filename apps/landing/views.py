from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import  messages
from django.core.mail import EmailMessage, get_connection, send_mail, BadHeaderError
from .models import Proyectos, Profesional, Experiencia
# Create your views here.



def index (request):
    if request.method=="GET":
        path = request.get_full_path 
        proyectos = Proyectos.objects.all()
        #Obtener el ultimo profesional
        profesional = Profesional.objects.all().order_by('-fecha_creacion')[0]
        experiencia = Experiencia.objects.all().order_by('-fecha')
        n_experiencia = experiencia.count()
        email_profesional = profesional.correo

        context ={
            'proyectos': proyectos,
            'profesional':profesional,
            'experiencia':experiencia,
            'n_experiencia':n_experiencia
        }

        return render (request ,'Home/index.html',context )

    if request.method =="POST":
        proyectos = Proyectos.objects.all()
        #Obtener el ultimo profesional
        profesional = Profesional.objects.all().order_by('-fecha_creacion')[0]
        experiencia = Experiencia.objects.all().order_by('-fecha')
        n_experiencia = experiencia.count()
        email_profesional = profesional.correo

        context ={
            'proyectos': proyectos,
            'profesional':profesional,
            'experiencia':experiencia,
            'n_experiencia':n_experiencia
        }
        profesional = Profesional.objects.all().order_by('-fecha_creacion')[0]

        email_profesional = profesional.correo

        name = request.POST['name']
    
        correo = request.POST['email']
        subject= request.POST['subject']
        message =request.POST['message']

        current_site= get_current_site(request)

        subject_conf="Formulario JO desarrollador"
        
        correo_admin = email_profesional

        correo_html = render_to_string('emails/email_client.html', {
            'name':name,
            'domain': current_site.domain,

        })
        correo_html_admin = render_to_string('emails/email_admin.html', {
            'name':name,
            'email_client':correo,
            'subject':subject,
            'message':message,
            'domain': current_site.domain,
            

        })

        text_content = strip_tags(correo_html)

        text_content_admin = strip_tags(correo_html_admin)


        email = EmailMultiAlternatives(
                    subject_conf,text_content,
                                to=[correo])
        email_admin=EmailMultiAlternatives(
                    subject,text_content_admin,
                                to=[correo_admin])
        
        email_admin.fail_silenty=False
        email_admin.attach_alternative(correo_html_admin,'text/html')
        email_admin.send()

        email.fail_silenty=False
        email.attach_alternative(correo_html,'text/html')
        email.send()

        messages.success(request,"Se realizado con exito el envio del formulario")
        return render (request ,'Home/index.html' ,context)