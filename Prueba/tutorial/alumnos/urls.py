from django.urls import path 
from .view import alumnos,alumno_detalle 


ultpatterns = [
            path ('alumnos/',alumnos,name='alumnos'),
            path('alumnos/<int:pk>',alumno_detalle,name='alumno_detalle')

]