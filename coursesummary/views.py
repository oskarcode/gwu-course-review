from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import CourseList

# Create your views here.


class CourseView(ListView):
    model= CourseList
    template_name = 'course/home.html'
    

class CourseDetailView(DetailView):
    model = CourseList
    context_object_name = 'course_detail'
    template_name = 'course/detail.html'
    
    


