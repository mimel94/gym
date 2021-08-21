from django import forms
from .models import Usuario, ValoracionMedica
from django.contrib.auth.forms import AuthenticationForm

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='Nombre de Usuario'
        self.fields['password'].widget.attrs['class']='form-control'
        self.fields['password'].widget.attrs['placeholder']='Contraseña'
            

class controlUsuarioForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(controlUsuarioForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }

    class Meta:
        model = Usuario
        fields = '__all__'

class valoracionMedicaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(valoracionMedicaForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }

    class Meta:
        model = ValoracionMedica
        fields = '__all__'



