from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response 
from .models import * 
from .serializers import * 

class New(APIView):
    def get(self, request):
        resl = Cars.objects.all()
        serializer = CarsSerializer(resl, many = True)
        return Response(serializer.data)
        print('asa')

class Admin(APIView):
    def post(self, request):
        serializer = CarsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        error = ({'error': 'ERRRRR'})
        

        return Response(error)
