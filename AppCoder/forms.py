from django import forms

class CursoFormulario(forms.Form):
    #Especificar los campos
    curso= forms.CharField()
    comision= forms.IntegerField()
