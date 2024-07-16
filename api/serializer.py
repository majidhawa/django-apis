from rest_framework import serializers
from students.models import Student
from teachers.models import Teacher
from courses.models import Course
from classPeriod.models import ClassPeriod
from classes.models import Class


class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'
        
class TeacherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teacher
        fields = '__all__'
        
class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = '__all__'

class ClassPeriodSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ClassPeriod
        fields = '__all__'

class ClassSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Class
        fields = '__all__'





