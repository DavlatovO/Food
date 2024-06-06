from rest_framework import serializers
from .import models

class FoodTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.FoodType
        fields = ['name']

class FoodSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Food
        fields = ['type', 'name', 'recipe', 'price' ]        

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ['text', 'food', 'author', 'created' ]        