from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Ejercicios(models.Model):
    nombre = models.CharField("Ejercicio",max_length=254)
    duracion = models.CharField("Duracion",max_length=254)
    series = models.CharField("Series",max_length=254)
    repeticiones = models.CharField("Repeticiones por serie",max_length=254)
    descanso = models.CharField("Descanso",max_length=254)

    def __str__(self) :
        return f'{self.nombre}'

class Rutina(models.Model):
    nombre = models.CharField("Rutina",max_length=254)
    lunes = models.ManyToManyField( Ejercicios,related_name='lunes')
    Martes = models.ManyToManyField( Ejercicios,related_name='martes')
    Miercoles = models.ManyToManyField( Ejercicios,related_name='miercoles')
    Jueves = models.ManyToManyField( Ejercicios, related_name='jueves')
    Viernes = models.ManyToManyField( Ejercicios, related_name='viernes')
    Sabado = models.ManyToManyField( Ejercicios, related_name='sabado')
    Domingo = models.ManyToManyField( Ejercicios,blank=True,related_name='domingo')

    def __str__(self) :
        return f'{self.nombre}'

class Plan(models.Model):

    def __str__(self):
        return self.nombre
    
    nombre = models.CharField( max_length=50 )
    valor = models.IntegerField()
    estado = models.BooleanField(default=True)   

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
    plan = models.ForeignKey(Plan,on_delete=models.CASCADE,null=True,blank=True)
    ocupacion = models.CharField( max_length=50,null=True,blank=True)            
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE,null=True,blank=True)
    entrenador = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    estado = models.BooleanField("estado", default= True)
    meses = models.IntegerField("Meses a pagar",null=True,blank=True)
    rutina = models.ForeignKey(Rutina,on_delete=models.CASCADE,blank=True,null=True)
    foto =  models.ImageField("Foto",upload_to="sitios", null=True)
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
    usuario = models.OneToOneField(Usuario, primary_key = True, on_delete=models.CASCADE,blank=True)    
    altura = models.CharField( max_length=50)
    peso = models.CharField(max_length=50)
    enfermedad = models.CharField(max_length=150)
    alergia = models.CharField(max_length=150)
    operaciones = models.CharField( max_length=150)


    