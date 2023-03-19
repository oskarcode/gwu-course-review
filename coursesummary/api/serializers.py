
from rest_framework import serializers
from coursesummary.models import CourseList


class CourseListSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourseList
        fields = '__all__'
        
        
