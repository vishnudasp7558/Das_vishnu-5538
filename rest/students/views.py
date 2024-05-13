from django.shortcuts import render
from students.models import student
from students.serializers import studentserializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET","POST"])
def allstudents(request):
    if(request.method=="GET"):
        s=student.objects.all() #Reads data from student table
        stu=studentserializer(s,many=True) #serializes data into json
        return Response(stu.data)  #sends json data as response
    elif(request.method=="POST"):
        s=studentserializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data,status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def studentsdetalis(request,pk):
    try:
        s=students.object.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUNT)
    if(request.method=="GET"):
        stu=studentserializer(s)
        return Response(stu.data)
