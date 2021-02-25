from django.db import models

# Create your models here.

class Plan(models.Model):

    def __str__(self):
        return self.nombre
    
    nombre = models.CharField( max_length=50 )
    valor = models.IntegerField()

class Sucursal(models.Model):
    def __str__(self):
        return self.nombre
    
    nombre = models.CharField( max_length=50 )    
 
class Usuario(models.Model):

    def __str__(self):
        return self.nombre + ' '+ self.apellido
    

    TIPO_DOCUMENTOS = (
        ('ti', 'Tarjeta de identidad'),
        ('cc', 'Cedula de ciudadania'),
    )    
    tipo_documento = models.CharField( max_length=50, choices=TIPO_DOCUMENTOS)
    numero_documento = models.IntegerField( primary_key = True, unique=True )
    nombre = models.CharField( max_length=50 )
    apellido = models.CharField( max_length=50 )    
    edad = models.IntegerField()
    plan = models.ForeignKey(Plan,on_delete=models.CASCADE)
    ocupacion = models.CharField( max_length=50 )            
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    estado = models.BooleanField("estado", default= True)
    
class ValoracionMedica(models.Model):  
    usuario = models.OneToOneField(Usuario, primary_key = True, on_delete=models.CASCADE)    
    altura = models.CharField( max_length=50)
    peso = models.CharField(max_length=50)
    enfermedad = models.CharField(max_length=150)
    alergia = models.CharField(max_length=150)
    operaciones = models.CharField( max_length=150)