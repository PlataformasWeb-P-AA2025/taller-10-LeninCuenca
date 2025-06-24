from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Parroquia(models.Model):
    UBICACION_CHOICES = [
        ('norte', 'Norte'),
        ('sur', 'Sur'),
        ('este', 'Este'),
        ('oeste', 'Oeste'),
    ]
    TIPO_CHOICES = [
        ('urbana', 'Urbana'),
        ('rural', 'Rural'),
    ]
    nombre = models.CharField(max_length=100, unique=True)
    ubicacion = models.CharField(max_length=10, choices=UBICACION_CHOICES)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    def __str__(self):
        return self.nombre

class Barrio(models.Model):
    NUMERO_PARQUES_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'), 
        (5, '5'),
        (6, '6'),
    ]      
    nombre = models.CharField(max_length=100, unique=True)
    numero_viviendas = models.IntegerField()
    numero_parques = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    numero_edificios_residenciales = models.CharField(max_length=100, choices=NUMERO_PARQUES_CHOICES)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre