import email
from rest_framework import serializers
from django.contrib.auth.models import User

#creacion de la clase para el registro

class RegisterSerializer(serializers.Serializer):
    username= serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    #metodo para crear usuario 
    def create(self, validate_data):
        instance = User()
        instance.username = validate_data.get('username')
        instance.email = validate_data.get('email')
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance


        def validate_username(self, data):
            users = User.objects.filter(username = data)
            if(len(users)!=0):
                raise serializers.ValidationError("Este nombre ya existe")
            else:
                return data
