from django.forms import ValidationError
from rest_framework import serializers
from .models import Account
from django.contrib.auth import get_user_model

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'phone')


UserModel = get_user_model()

class NewAccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ("username", "email", "password", "password2")

    def validate(self, data):
        if data['password'] != data['password2']:
            raise ValidationError({'password': "Passwords must match"})
        
        return data

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password = validated_data['password'],
        )
        return user
    

    # password2 = serializers.CharField(
    #     style={'input_type': 'password'}, write_only=True)

    # class Meta:
    #     model = Account
    #     fields = ('username', 'email', 'password', 'password2',)
    #     extra_kwargs = {
    #         'password': {'write_only': True}
    #     }

    # def save(self):
    #     # try:
    #     new_account = Account(
    #         email= self.validated_data['email'].lower(),
    #         username= self.validated_data['username'],
    #     )

    #     if Account.objects.filter(email=self.validated_data['email'].lower()).exists():
    #         raise serializers.ValidationError(
    #             {'email': ['Account with this email already exists.']})

    #     password = self.validated_data['password']
    #     password2 = self.validated_data['password2']

    #     if password != password2:
    #         raise serializers.ValidationError(
    #             {'password': ['Passwords must match.']})

    #     new_account.set_password(password)
    #     new_account.save()
    #     return new_account