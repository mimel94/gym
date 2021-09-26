from django.db import models
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.urls import reverse
from django.views.generic.edit import CreateView, FormView, UpdateView

from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth import login,logout
from django.http import HttpResponseRedirect

from .models import Ejercicios, Plan, Rutina, Sucursal, Usuario, ValoracionMedica
from .forms import FormularioLogin, PlanForm, controlUsuarioForm, valoracionMedicaForm,SucursalForm, RutinaForm, EjerciciosForm
from django.views.generic import TemplateView, CreateView, ListView,DetailView
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
    template_name = 'dashboard/actualizar_sucursal.html'
    success_url = reverse_lazy('listar_sucursales')

class CrearEntrenador(CreateView):
    model = Usuario
    template_name = 'dashboard/crear_entrenador.html'
    form_class = controlUsuarioForm
    success_url = reverse_lazy('listar_entrenador')

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
    success_url = reverse_lazy('listar_entrenador') 

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
    template_name = 'dashboard/actualizar_plan.html'
    form_class = PlanForm
    success_url = reverse_lazy('listar_plan')

class CrearvaloracionMedica(CreateView):
    model = ValoracionMedica
    template_name = 'dashboard/valoracion_medica.html'            
    form_class = valoracionMedicaForm
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        id = self.kwargs['id']
        usuario = Usuario.objects.get(pk = id)    
        return {'usuario':usuario}

    def form_valid(self, form):
        id_user = self.kwargs['id']
        print("ID USUARIO",id_user)
        form.instance.usuario = Usuario.objects.get(pk=id_user)
        return super().form_valid(form)          

class DetallevaloracionMedica(DetailView):
    model = ValoracionMedica
    template_name = 'dashboard/detalle_valoracion_medica.html'
    # form_class = valoracionMedicaForm
    # success_url = reverse_lazy('dashboard')
    
    def dispatch(self, request, *args, **kwargs):
        id = self.kwargs['id']
        usuario = Usuario.objects.get(pk = id)        
        try:
            ValoracionMedica.objects.get(usuario=usuario)
        except:
            return redirect('crear_valoracion_medica', id = id)

        self.get_object()

        return super(DetallevaloracionMedica,self).get(request, *args, **kwargs)
    
    def get_object(self):
        try:
            # self.object = self.kwargs['id']
            self.object = self.model.objects.get(usuario__id=self.kwargs['id'])
        except:
            pass
        return self.object

class ActualizarValoracionMedica(UpdateView):
    model = ValoracionMedica
    template_name = 'dashboard/actualizar_medica.html'            
    form_class = valoracionMedicaForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        id_user = self.kwargs['pk']
        print("ID USUARIO",id_user)
        form.instance.usuario = Usuario.objects.get(pk=id_user)
        return super().form_valid(form)          

class VerPerfilUsuario(TemplateView):
    model = Usuario
    template_name = 'dashboard/ver_perfil.html'

class EditarUsuarioPropio(UpdateView):
    model = Usuario
    form_class = controlUsuarioForm
    template_name = 'dashboard/actualizar_perfil.html'    
    success_url = reverse_lazy('dashboard')

    # def dispatch(self, request, *args, **kwargs):
    #     id = self.kwargs['pk']
    #     if id == request.user.id:
    #         self.get_object()
    #     else:      
    #         return redirect('mi_perfil')

    #     self.get_object()
    #     return super(EditarUsuarioPropio,self).get(request, *args, **kwargs)
    
    # def get_object(self,queryset=None):        
    #     object = getattr(self, 'object', None)
    #     if object is None:
    #         object = super().get_object(queryset)   
    #     return object

def preciosView(request):
    return render(request, 'web/precios.html')

class CrearRutina(CreateView):
    model = Rutina
    template_name = 'dashboard/crear_rutina.html'
    form_class = RutinaForm
    success_url = reverse_lazy('listar_rutinas')

class EditarRutina(UpdateView):
    model = Rutina
    form_class = RutinaForm
    template_name = 'dashboard/actualizar_rutina.html'
    success_url = reverse_lazy('listar_rutinas')

class ListarRutinas(ListView):
    model = Rutina
    template_name = 'dashboard/listar_rutina.html'
    paginate_by = 50

class CrearEjercicio(CreateView):
    model = Ejercicios
    form_class = EjerciciosForm
    template_name = 'dashboard/crear_ejercicio.html'
    success_url = reverse_lazy('listar_ejercicios')

class ActualizarEjercicio(UpdateView):
    model = Ejercicios
    form_class = EjerciciosForm
    template_name = 'dashboard/actualizar_ejercicio.html'
    success_url = reverse_lazy('listar_ejercicios')

class ListarEjercicios(ListView):
    model = Ejercicios
    template_name ='dashboard/listar_ejercicio.html'
    paginate_by = 50

class RutinaUsuario(TemplateView):    
    template_name = 'dashboard/rutina_usuario.html'
    
    def get_context_data(self, **kwargs):
        context = super(RutinaUsuario, self).get_context_data(**kwargs)   
        pk_user = kwargs["pk"]
        usuario = Usuario.objects.get(pk=pk_user)
        context["usuario"] = usuario
        rutinas = Rutina.objects.all()
        context["rutinas"] = rutinas        
        return context

    def post(self, request, *args, **kwargs):
        pk_usuario = request.POST.get("pk_usuario")
        pk_rutina = request.POST.get("pk_rutina")
        print(pk_rutina)

        usuario = Usuario.objects.get(pk=pk_usuario)
        rutina_usuario = Rutina.objects.get(pk=pk_rutina)
        usuario.rutina = rutina_usuario
        usuario.save()
        return HttpResponseRedirect(reverse('dashboard'))


