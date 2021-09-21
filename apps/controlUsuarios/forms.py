from django import forms
from .models import Plan, Sucursal, Usuario, ValoracionMedica, Ejercicios, Rutina
from django.contrib.auth.forms import AuthenticationForm

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='p-4 input'
        self.fields['username'].widget.attrs['placeholder']=''
        self.fields['password'].widget.attrs['class']='p-4 input'
        self.fields['password'].widget.attrs['placeholder']='*********'
            

class controlUsuarioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(controlUsuarioForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'entrenador':
                self.fields[field].widget.attrs = {
                    'class': 'form-check'
                }
            else:    
                self.fields[field].widget.attrs = {
                    'class': 'form-control'
                }
    
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs={
           'class': 'form-control',
           'placeholder':'Ingrese la contraseña',
           'required':'required',
        }
    ))
    password2 = forms.CharField(label='Contraseña de confirmación', widget=forms.PasswordInput(
        attrs={
           'class': 'form-control',
           'placeholder':'Ingrese nuevamente la contraseña ',
           'required':'required',
        }
    ))

    class Meta:
        model = Usuario
        fields = ('username','email','tipo_documento','numero_documento','nombre','apellidos','edad','plan','ocupacion','sucursal','entrenador','meses')
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError("Contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class SucursalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SucursalForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'estado':
                self.fields[field].widget.attrs = {
                    'class': 'form-check'
                }
            else:
                self.fields[field].widget.attrs = {
                    'class': 'form-control'
                }

    class Meta:
        model = Sucursal
        fields = '__all__'

class PlanForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PlanForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'estado':
                self.fields[field].widget.attrs = {
                    'class': 'form-check'
                }
            else:
                self.fields[field].widget.attrs = {
                    'class': 'form-control'
                }

    class Meta:
        model = Plan
        fields = '__all__'

class valoracionMedicaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(valoracionMedicaForm, self).__init__(*args, **kwargs)        
        for field in self.fields:
            if field == 'usuario':
                self.fields[field].widget.attrs = {
                    'disabled': 'disabled',
                    'class': 'form-control'
                }
            else:
                self.fields[field].widget.attrs = {
                    'class': 'form-control'
                }
        # self.fields['usuario'].widget.attrs['disabled']='disabled'

    class Meta:
        model = ValoracionMedica
        fields = '__all__'

class EjerciciosForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EjerciciosForm, self).__init__(*args, **kwargs)
        for field in self.fields:        
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }

    class Meta:
        model = Ejercicios
        fields = '__all__'

class RutinaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RutinaForm, self).__init__(*args, **kwargs)
        for field in self.fields:        
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }

    class Meta:
        model = Rutina
        fields = '__all__'

