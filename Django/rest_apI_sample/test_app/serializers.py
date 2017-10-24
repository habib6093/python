from rest_framework import serializers
from .models import post


class showdata(serializers.ModelSerializer):

   class Meta:
       model=post
       fields = ('title','author')
