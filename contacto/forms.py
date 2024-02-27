from django import forms

class formularioContacto(forms.Form):
    nombre=forms.CharField(label='Nombre',required=True)
    mail=forms.EmailField(label='Correo',required=True)
    contenido=forms.CharField(label='Contenido',widget=forms.Textarea)