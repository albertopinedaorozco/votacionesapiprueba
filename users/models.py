#django libraries
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from locaciones.models import Municipio


class UserModel(models.Model):
    creado = models.DateTimeField(
        'Creado el',
        auto_now_add=True
    )
    modificado = models.DateTimeField(
        'Modificado',
        auto_now=True
    )

    class Meta:
        abstract = True
        get_latest_by = 'creado'
        ordering = ['-creado', '-modificado']


class User(UserModel, AbstractUser):
    
    celular_regex = RegexValidator(
        regex= r'\+?1?\d{9,15}$',
        message = 'El numero celular debe ser ingresado en el formato: +999999999. de 9 a 15 digitos'
    )
    numero_celular = models.CharField(validators=[celular_regex], max_length=17, blank=True)
    direccion = models.CharField(max_length=70,blank=True)
    municipio = models.ForeignKey(Municipio, on_delete = models.CASCADE,blank=True,null=True)
    
    #USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name','last_name']

    es_lider = models.BooleanField(
        '¿ Es lider ?',
        default = True,
        help_text=(
            'Ayuda a distinguir usuarios y realizar consultas '
            'El lider es el principal tipo de usuario'
        )
    )

    foto = models.ImageField(
        'foto de perfil',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )


    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
       

    #datos
    votantes_registrados = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.user)
