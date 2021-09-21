"""powergym URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.controlUsuarios.views import inicio, CrearUsuario, \
                                EditarUsuario,\
                                CrearSucursal,ListarSucursal, ActualizarSucursal,\
                                CrearEntrenador, ListarEntrenador, ActualizarEntrenador,\
                                CrearvaloracionMedica,DetallevaloracionMedica, ActualizarValoracionMedica, \
                                ListarPlan,CrearPlan,ActualizarPlan,\
                                preciosView,Dashboard, Login, logout_usuario



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio, name='index'),
    path("accounts/login/",Login.as_view(),name='login'),
    path("logout/",login_required(logout_usuario), name="logout"),

    path("dashboard/",login_required(Dashboard.as_view()),name="dashboard"),
    path('dashboard/crearUsuario/', login_required(CrearUsuario.as_view()), name='crear_usuario'),    
    path('dashboard/actualizarUsuario/<int:pk>/', login_required(EditarUsuario.as_view()), name='actualizar_usuario'),

    path('dashboard/crearSucursal/', login_required(CrearSucursal.as_view()), name='crear_sucursal'),
    path('dashboard/listarSucursal/',login_required(ListarSucursal.as_view()), name='listar_sucursales'),
    path('dashboard/actualizarSucursal/<int:pk>/', login_required(ActualizarSucursal.as_view()), name='actualizar_sucursal'),

    path('dashboard/crearEntrenador/',login_required( CrearEntrenador.as_view()), name='crear_entrenador'),
    path('dashboard/listarEntrenador/',login_required(ListarEntrenador.as_view()), name='listar_entrenador'),
    path('dashboard/actualizarEntrenador/<int:pk>/', login_required(ActualizarEntrenador.as_view()), name='actualizar_entrenador'),

    path('dashboard/listarPlan/', login_required(ListarPlan.as_view()), name='listar_plan'),
    path('dashboard/crearPlan/', login_required(CrearPlan.as_view()), name='crear_plan'),
    path('dashboard/ActualizarPlan/<int:pk>/',login_required( ActualizarPlan.as_view()), name='actualizar_plan'),
   
    path('dashboard/CrearValoracionMedica/<int:id>/', login_required(CrearvaloracionMedica.as_view()), name='crear_valoracion_medica'),
    path('dashboard/DetalleValoracionMedica/<int:id>/',login_required( DetallevaloracionMedica.as_view()), name='detalle_valoracion_medica'),
    path('dashboard/ActualizarValoracionMedica/<int:pk>/',login_required( ActualizarValoracionMedica.as_view()), name='actualizar_valoracion_medica'),
    
    path('precios/',preciosView, name='precios'),
  

]
