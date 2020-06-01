#django 
from django.contrib.auth import password_validation
from django.core.validators import RegexValidator
from .models import User, Profile


#rest_framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

#apps
from locaciones.models import Municipio

#thirds
import requests


class UserSerializer(serializers.ModelSerializer): # new
    Georeff = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('id', 'username','first_name','last_name','email','numero_celular','direccion','municipio','foto','Georeff')

    def get_Georeff(self, obj):

        #try:
            # api-endpoint 
            URL = "https://maps.googleapis.com/maps/api/geocode/json"
            
            # location given here 
            location = obj.direccion #"1600+Amphitheatre+Parkway,+Mountain+View,+CA"
            
            # defining a params dict for the parameters to be sent to the API 
            PARAMS = {'address':location, 'key': 'AIzaSyB_33P2YTOwWHS8FEGykm2u1Tx7BA9CjPo'} 
            
            # sending get request and saving the response as response object 
            r = requests.get(url = URL, params = PARAMS) 
            
            # extracting data in json format 
            data = r.json() 
                    
            # extracting latitude, longitude and formatted address  
            # of the first matching location 
            latitude = data['results'][0]['geometry']['location']['lat'] 
            longitude = data['results'][0]['geometry']['location']['lng'] 
            formatted_address = data['results'][0]['formatted_address'] 
            
        
            return ("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
                %(latitude, longitude,formatted_address))
        
        # except:
        #     return ""
            
            
        
        


class UserSignUpSerializer(serializers.Serializer):
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators = [UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        validators = [UniqueValidator(queryset=User.objects.all())]
    )
    celular_regex = RegexValidator(
        regex= r'\+?1?\d{9,15}$',
        message = 'El numero celular debe ser ingresado en el formato: +999999999. de 9 a 15 digitos'
    )
    numero_celular = serializers.CharField(validators=[celular_regex], max_length=17)

    #password
    password = serializers.CharField(
        min_length=4,
        max_length=64
    )
    password_confirmation = serializers.CharField(
        min_length=4,
        max_length=64
    )
    #nombres
    first_name = serializers.CharField(min_length=2,max_length=30 )
    last_name = serializers.CharField(min_length=2,max_length=30 )

    #ubicacion
    direccion = serializers.CharField(min_length=2,max_length=30 )
    #municipio =  serializers.RelatedField(source='Municipio', queryset=Municipio.objects.all())
    municipio =  serializers.RelatedField(read_only=True,source='Municipio')
    foto = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=True)

    
    def validate(self,data):
        passwd = data['password']
        passwd_conf= data['password_confirmation']

        if passwd != passwd_conf:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        
        password_validation.validate_password(passwd) 
        return data

    def create(self,data):
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        profile = Profile.objects.create(user=user)# aux model for user
                
        return user

