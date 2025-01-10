from .models import *
from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields=(
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "phone_number",
            "role",
            "payment_status",
            "ca_code",
            "date_joined"
        )
    def create(self, validated_data):
        phone_number = validated_data.get('phone_number', '')
        # Ensure phone number has the +91 prefix, only if provided
        if phone_number:
            phone_number = f"+91{phone_number}"

        user = Users.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone_number=phone_number,
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            role=validated_data['role'],
            payment_status=validated_data['payment_status'],
        )
        return user
    

class Get_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields=(
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "phone_number",
            "role",
            "payment_status",
            "ca_code",
        )

class ContingentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contingent
        fields="__all__"
        extra_kwargs = {'user': {'read_only': True}}

class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields="__all__"
        extra_kwargs = {'user': {'read_only': True}}


class StartupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startup
        fields="__all__"
        extra_kwargs = {'user': {'read_only': True}}


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields="__all__"
        extra_kwargs = {'user': {'read_only': True}}


class CASerializer(serializers.ModelSerializer):
    class Meta:
        model = CA
        fields="__all__"
        extra_kwargs = {'user': {'read_only': True}}


