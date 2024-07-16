from django.db import models
from courses.models import Course
from classes.models import Class

class ClassPeriod(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Class, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.start_time}-{self.end_time}"
