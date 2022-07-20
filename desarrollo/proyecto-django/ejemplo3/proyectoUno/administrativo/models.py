from django.db import models

# Create your models here.

class Propietario(models.Model):
    tipo = (('ecuatoriana','Ecuatoriana'),('peruana','Peruana'), ('colombiana','Colombiana'))
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=30, choices=tipo)

    def __str__(self):
        return "%s %s %d %s" % (self.nombre,
                self.apellido,
                self.edad,
                self.nacionalidad)

class Departamento(models.Model):
    costo = models.DecimalField(max_digits=100, decimal_places=2)
    cuartos = models.IntegerField()
    banios = models.IntegerField()
    alicuota = models.CharField(max_length=100)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE,
            related_name="departamentos")

    def __str__(self):
        return "%d %d %d %d" % (self.costo, self.cuartos, self.banios, self.alicuota)
