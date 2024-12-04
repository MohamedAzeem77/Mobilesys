from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import mobile
from .serializers import MobileSerializer


class MobileCreateViews(APIView):
    def post(self,request):
        serializer=MobileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def get(self,request):
        mobile1=mobile.objects.all()
        serializer=MobileSerializer(mobile1,many=True)
        return Response(serializer.data)
    


class MobileListViews(APIView):
    def get(self,request,pk):
        try:
            mobile1=mobile.objects.get(pk=pk)
            serializer=MobileSerializer(mobile1)
            return Response(serializer.data)
        except mobile.DoesNotExist:
            return Response({'error':'mobile not found'},status=status.HTTP_404_NOT_FOUND)
        
    
    def put(self,request,pk):
        try:
            mobile1=mobile.objects.get(pk=pk)
            serializer=MobileSerializer(mobile1,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except mobile.DoesNotExist:
            return Response({'error':'mobile not found'},status=status.HTTP_404_NOT_FOUND)
        

    def delete(self, request, pk):
        try:
            mobile1 = mobile.objects.get(pk=pk)
            mobile1.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except mobile.DoesNotExist:
            return Response({'error': 'mobile not found'}, status=status.HTTP_404_NOT_FOUND)
