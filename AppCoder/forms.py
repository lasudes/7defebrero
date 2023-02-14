from django import forms

class estudiantesform(forms.Form):
    
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()

class profesoresform(forms.Form):
    
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    profesion = forms.CharField(max_length=20)

class cursoform(forms.Form):
    
    tipo = forms.CharField(max_length=40)
    comision = forms.IntegerField()
    duracion = forms.IntegerField()

    