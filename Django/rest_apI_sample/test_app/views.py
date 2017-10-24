from django.shortcuts import render
from rest_framework.views import APIView
from .models import post
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import showdata


# Create your views here.


class postlist(APIView):

     def get(self,request):
         posts=post.objects.all()
         serializer=showdata(posts,many=True)
         return Response(serializer.data)

     def post(self):
         pass