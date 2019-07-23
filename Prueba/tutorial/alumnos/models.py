from django.db import models

# Create your models here.

class Alumno(model.Model):
    nombre=models.Charfield(max_lenght=50)  
    email=model.IntegerField()

    def __str__ (self):
        return '{}'.format(self.nombre)
    class Meta:
        verbose_name_plural = "Alumnos"