from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class Plan(models.Model):

    def __str__(self):
        return self.nombre
    
    nombre = models.CharField( max_length=50 )
    valor = models.IntegerField()

class Sucursal(models.Model):
    def __str__(self):
        return self.nombre
    
    nombre = models.CharField(default = "",max_length=50 )
    direccion = models.CharField(default = "",max_length=250)
    telefono = models.CharField(default = "",max_length=250)    
    estado = models.BooleanField(default=True)   

class UsuarioManager(BaseUserManager):
    def create_user(self,email,username,nombre,apellidos,numero_documento, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electronico')
        usuario = self.model(
                username = username, 
                email = self.normalize_email(email), 
                nombre = nombre, 
                apellidos = apellidos,
                numero_documento = numero_documento
                )
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self,email,username,nombre,apellidos,numero_documento, password):
        usuario = self.create_user(
            email, 
            username = username,             
            nombre = nombre, 
            apellidos = apellidos,
            numero_documento = numero_documento,
            password=password
        )
        usuario.admin = True
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser): 

    TIPO_DOCUMENTOS = (
        ('ti', 'Tarjeta de identidad'),
        ('cc', 'Cedula de ciudadania'),
    )    
    username = models.CharField('Nombre de usuario', unique=True, max_length=100)
    email = models.EmailField('Correo Electronico', max_length=254, unique=True)
    tipo_documento = models.CharField('Tipo de documento', max_length=50, choices=TIPO_DOCUMENTOS,null=True)
    numero_documento = models.IntegerField('Numero de documento', unique=True)
    nombre = models.CharField('Nombre', max_length=50 )
    apellidos = models.CharField('Apellidos', max_length=50)    
    edad = models.IntegerField('Edad',null=True)
    plan = models.ForeignKey(Plan,on_delete=models.CASCADE,null=True)
    ocupacion = models.CharField( max_length=50,null=True)            
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE,null=True)
    entrenador = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    estado = models.BooleanField("estado", default= True)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','numero_documento','nombre','apellidos']

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.admin
 
class ValoracionMedica(models.Model):  
    usuario = models.OneToOneField(Usuario, primary_key = True, on_delete=models.CASCADE)    
    altura = models.CharField( max_length=50)
    peso = models.CharField(max_length=50)
    enfermedad = models.CharField(max_length=150)
    alergia = models.CharField(max_length=150)
    operaciones = models.CharField( max_length=150)