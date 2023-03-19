
from coursesummary.models import CourseList
from django.views import generic
from rest_framework import viewsets
from .serializers import CourseListSerializers
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions



class CourseListSer(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = CourseList.objects.all()
    serializer_class = CourseListSerializers
    
    
    
class CourseCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = CourseList.objects.all()
    serializer_class = CourseListSerializers
    
    