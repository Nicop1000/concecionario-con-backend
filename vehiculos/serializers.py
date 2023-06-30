from rest_framework import serializers
from .models import vehiculo, imagenvehiculo, caracteristicas, team

class teamSerializer(serializers.ModelSerializer):
      class Meta:
            model = team
            fields = '__all__'

class caracteristicasSerializer(serializers.ModelSerializer):
      
      class Meta:
            model = caracteristicas
            fields = ['id', 'caracteristica']

class imagenvehiculoSerializer(serializers.ModelSerializer):
        
       class Meta:
            model = imagenvehiculo
            fields = ['id', 'imagen']  

class vehiculoSerializer(serializers.ModelSerializer):
       
        imagenes =  imagenvehiculoSerializer(many=True, read_only=True)
        caracteristicas = caracteristicasSerializer(many=True, read_only=True)

        class Meta:
            model = vehiculo
            fields = ['id', 'name', 'price', 'description', 'imagen_principal', 'imagenes', 'caracteristicas']