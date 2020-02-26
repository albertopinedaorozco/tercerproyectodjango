from django.db import models

class Estudiante(models.Model):
    edad = models.IntegerField()
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=100)
    observaciones = models.TextField(max_length=500)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    horas = models.IntegerField()

    def __str__(self):
        return self.nombre

class Docente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)

    def __str__(self):
        return "{0}, {1}".format(self.nombre, self.apellido)

class Programa(models.Model):
    nombre = models.CharField(max_length=100)
    semestres = models.IntegerField()

    def __str__(self):
        return self.nombre


