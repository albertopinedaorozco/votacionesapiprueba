from django.db import models

from users.models import UserModel,User
from locaciones.models import Comuna, Barrio, PuestoVotacion

class Votante(UserModel,models.Model):
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    direccion = models.CharField(max_length=60)
    num_cedula = models.CharField(max_length=20)
    barrio = models.ForeignKey(Barrio, on_delete = models.CASCADE)
    puesto_votacion = models.ForeignKey(PuestoVotacion, on_delete = models.CASCADE)
    mesa = models.CharField(max_length=4)
    lider = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.nombres, self.apellidos)

