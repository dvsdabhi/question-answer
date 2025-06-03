from rest_framework import serializers
from .models import *

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name', 'icon']

class questionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question', 'answer', 'language', 'difficulty']
        
class CareerAdviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerAdvice
        fields = ['id', 'title', 'description', 'category', 'order', 'image']
