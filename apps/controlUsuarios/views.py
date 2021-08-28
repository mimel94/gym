from django.db import models
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView, FormView, UpdateView

from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth import login,logout
from django.http import HttpResponseRedirect

from .models import Plan, Sucursal, Usuario, ValoracionMedica
from .forms import FormularioLogin, PlanForm, controlUsuarioForm, valoracionMedicaForm,SucursalForm
from django.views.generic import TemplateView, CreateView, ListView
# Create your views here.

class Login(FormView):
    template_name = 'web/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('dashboard')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request,*args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)
    
def logout_usuario(request):
    logout(request)
    return HttpResponseRedirect('/')


def inicio(request):
    return render(request,'web/index.html')

class Dashboard(ListView):    
    model = Usuario
    template_name="dashboard/index.html"
    paginate_by = 10    

    def get_queryset(self):
        consulta = self.model.objects.filter(entrenador=False)
        return consulta    

class CrearUsuario(CreateView):
    model = Usuario
    template_name = 'dashboard/crear_clientes.html'
    form_class = controlUsuarioForm
    success_url = reverse_lazy('dashboard')

class EditarUsuario(UpdateView):
    model = Usuario
    form_class = controlUsuarioForm
    template_name = 'dashboard/actualizar_clientes.html'    
    success_url = reverse_lazy('dashboard')

class CrearSucursal(CreateView):
    model = Sucursal
    form_class = SucursalForm
    template_name = 'dashboard/crear_sucursal.html'
    success_url = reverse_lazy('listar_sucursales')

class ListarSucursal(ListView):
    model = Sucursal
    template_name = 'dashboard/listar_sucursales.html'
    paginate_by = 10

class ActualizarSucursal(UpdateView):
    model = Sucursal
    form_class = SucursalForm
    template_name = 'dashboard/crear_sucursal.html'
    success_url = reverse_lazy('listar_sucursales')

class CrearEntrenador(CreateView):
    model = Usuario
    template_name = 'dashboard/crear_entrenador.html'
    form_class = controlUsuarioForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.entrenador = True
        obj.save()
        return  redirect("listar_entrenador")

class ListarEntrenador(ListView):    
    model = Usuario
    template_name="dashboard/listar_entrenadores.html"   
    paginate_by = 10    

    def get_queryset(self):
        consulta = self.model.objects.filter(entrenador=True)
        return consulta

class ActualizarEntrenador(UpdateView):
    model = Usuario
    form_class = controlUsuarioForm
    template_name = 'dashboard/actualizar_entrenador.html'    
    success_url = reverse_lazy('dashboard') 

class ListarPlan(ListView):
    model = Plan
    template_name = 'dashboard/listar_plan.html'
    paginate_by = 10

class CrearPlan(CreateView):
    model = Plan
    template_name = 'dashboard/crear_plan.html'
    form_class = PlanForm
    success_url = reverse_lazy('listar_plan')

class ActualizarPlan(UpdateView):
    model = Plan
    template_name = 'dashboard/crear_plan.html'
    form_class = PlanForm
    success_url = reverse_lazy('listar_plan')

def valoracionMedica(request, id):
    usuario = Usuario.objects.get(numero_documento = id)
    try:
        valoracion = ValoracionMedica.objects.get(usuario=usuario)
    except:
        valoracion = None
    if request.method == 'GET':            
        form = valoracionMedicaForm(instance=valoracion)
        contexto = {
            'form':form
        }
    else:
        form = valoracionMedicaForm(request.POST, instance=valoracion)
        contexto = {
            'form':form
        }
        #print(form)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')

    return render(request,'web/valoracion_medica.html',contexto)

def preciosView(request):
    return render(request, 'web/precios.html')





