from django.shortcuts import render,redirect

from ProyectoWeb import settings
from .forms import formularioContacto
from django.core.mail import EmailMessage
from ProyectoWeb.settings import EMAIL_HOST_USER
#from contacto.models import Contacto

# Create your views here.

def contactos(request):
    miFormContacto=formularioContacto()
    #contactos=Contacto.objects.all()
    if request.method=='POST':
        miFormContacto=formularioContacto(data=request.POST)
        if miFormContacto.is_valid():
            nombre=request.POST.get("Nombre")
            correo=request.POST.get("Correo")
            contenido=request.POST.get("Contenido")

            email = EmailMessage(
                "Mensaje desde App Django",
                "El Usuario con nombre {} con la direccion {} escribe lo siguiente: \n\n{}".format(nombre,correo,contenido),
                EMAIL_HOST_USER,
                ['juanitoespin@gmail.com'],
                #reply_to=[correo],
            )
            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")
            
           
    return render(request,'contacto/contacto.html',{'miFormulario':miFormContacto})

