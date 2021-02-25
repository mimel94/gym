from django import forms
from .models import Usuario, ValoracionMedica

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



