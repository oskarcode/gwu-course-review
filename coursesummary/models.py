from django.db import models

# Create your models here.


class CourseList(models.Model):
    classname = models.CharField(max_length=100)
    classnumber = models.CharField(max_length=100)
    classlink = models.URLField(blank=True)
    summary = models.TextField(blank=True)
    
    def __str__(self):
        return f'This is a summary of {self.classname}'
    