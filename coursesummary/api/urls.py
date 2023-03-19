from django.urls import include, path
from coursesummary.api import views




urlpatterns = [
    path('courseapi/<int:pk>', views.CourseListSer.as_view(), name='api-course-list'),
    path('courseapi/create', views.CourseCreate.as_view(), name='api-course-create'),
    
]


