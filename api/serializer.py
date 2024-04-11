from .models import *
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import ValidationError


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        # fields = ['stol', 'product', 'quantity']
        fields = '__all__'


class StolSerializer(ModelSerializer):
    class Meta:
        model = Stol
        fields = '__all__'


class AboutUsSerializer(ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        depth = 3


class WaiterSerializer(ModelSerializer):
    class Meta:
        model = Waiter
        fields = '__all__'



# !-------------------------------------------Register Serializer----------------------------------------#
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=80)
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate(self, attrs):
        email_exsist = User.objects.filter(email=attrs['email']).exists()
        username_exsist = User.objects.filter(username=attrs['username']).exists()

        if email_exsist:
            raise ValidationError("Email has already been used")
        if username_exsist:
            raise ValidationError("Username has already been used")

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop('password')

        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
