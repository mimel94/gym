from django.shortcuts import render, redirect
from .models import Usuario, ValoracionMedica
from .forms import controlUsuarioForm, valoracionMedicaForm
# Create your views here.

def inicio(request):
    return render(request,'index.html')

def crearUsuario(request):
    if request.method == 'GET':            
        form = controlUsuarioForm
        contexto = {
            'form':form
        }
    else:
        form = controlUsuarioForm(request.POST)
        contexto = {
            'form':form
        }
        #print(form)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')

    return render(request,'crear_clientes.html',contexto)

def listarClientes(request):
    clientes = Usuario.objects.all()
    contexto = {
        'clientes':clientes
    }
    return render(request,'listar_clientes.html', contexto)

def editarUsuario(request, id):
    usuario = Usuario.objects.get(numero_documento = id)
    if request.method == 'GET':
        form = controlUsuarioForm(instance = usuario)
        contexto = {
            'form':form
        }
    else: 
        form = controlUsuarioForm(request.POST, instance= usuario )
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    return render(request, 'actualizar_clientes.html', contexto)

def eliminarUsuario(request, id):
    usuario = Usuario.objects.get(numero_documento=id)
    usuario.delete()
    return redirect('listar_clientes')

def valoracionMedica(request, id):
    usuario = Usuario.objects.get(numero_documento = id)
    valoracion = ValoracionMedica.objects.get(usuario=usuario)
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

    return render(request,'valoracion_medica.html',contexto)


