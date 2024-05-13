from rest_framework import serializers
from students.models import student

#This class is used for converting student objects into json object format
class studentserializer(serializers.ModelSerializer):

    class Meta:
        model=student
        fields='__all__'