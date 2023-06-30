from django.db import models

# Create your models here.

class vehiculo(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    imagen_principal = models.ImageField(upload_to='imagen_principal', null=True)

    def __str__(self):
     return self.name

class imagenvehiculo(models.Model):
    imagen = models.ImageField(upload_to="imagenes")
    vehiculo = models.ForeignKey(vehiculo, related_name='imagenes', on_delete=models.CASCADE)

class caracteristicas(models.Model):
   caracteristica = models.CharField(max_length=200, null=True)
   vehiculo = models.ForeignKey(vehiculo, related_name='caracteristicas', on_delete=models.CASCADE)

   def __str__(self):
     return self.caracteristica
   
class team(models.Model):
    name = models.CharField(max_length=200, blank=False, null=True)
    role = models.CharField(max_length=200, blank=False, null=True)
    imageUrl = models.ImageField(upload_to="imagenes", null=True)
    twitterUrl = models.CharField(max_length=200, blank=True, null=True)
    linkedinUrl = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
     return self.name