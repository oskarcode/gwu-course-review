from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.CourseView.as_view(), name = 'course-home'),
    path('course/<int:pk>', views.CourseDetailView.as_view(), name ='course-detail'),
]
