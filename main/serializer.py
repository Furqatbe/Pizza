from rest_framework import serializers
from .models import *

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'

class Welcome_textSerializer(serializers.ModelSerializer):
    class Meta:
        model = Welcome_text
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model =Service
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class AchievmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievment
        fields = '__all__'



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model =Cart
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model =Order
        fields = '__all__'