from django.contrib.auth.models import User

from rest_framework import serializers

from core.models import Phone, Brand


class PhoneSerializer(serializers.ModelSerializer):
    # built = serializers.SerializerMethodField(read_only = True)
    # brand = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Phone
        fields = "__all__"
        # depth = 2

    def get_built(self, obj):
        return obj.built.name
    
    def get_brand(self, obj):
        return obj.brand.name



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()



class RegisterSerializer(serializers.Serializer):
    username    = serializers.CharField(min_length=5)
    password    = serializers.CharField(min_length=8)
    password2   = serializers.CharField(min_length=8)

    def create(self, validated_data):
        
        username = validated_data.get("username")
        password = validated_data.get("password")
        user = User.objects.create_user(username, password=password)
        if user:
            return user
        raise serializers.ValidationError("failed to auth")

    def validate_username(self, value):
        if User.objects.filter(username=value):
            raise serializers.ValidationError("username exist")
        return value

    def validate_password(self, value):
        #TODO password validation
        return value

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("passwords are not match")
        return data
    

class BrandSerializer(serializers.ModelSerializer):
    nationality = serializers.SerializerMethodField()
    class Meta:
        model = Brand
        fields = ("id", "name", "nationality")
        
    def get_nationality(self, obj):
        return obj.country.name