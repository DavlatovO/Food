from django.shortcuts import render
from .import models
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import FoodSerializers, FoodTypeSerializers, CommentSerializers
from rest_framework import generics, mixins, viewsets
from rest_framework.decorators import action

class FoodTypeViewset(mixins.RetrieveModelMixin, 
                      mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    queryset = models.FoodType.objects.all()
    serializer_class = FoodTypeSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['get'])
    def custom_status(self, request):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)
        

class FoodViewset(viewsets.ModelViewSet):
    queryset = models.Food.objects.all()
    serializer_class = FoodSerializers
    
class CommentViewset(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = CommentSerializers

