from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import StudentSerializer
from .serializer import TeacherSerializer
from .serializer import CourseSerializer
from .serializer import ClassPeriodSerializer
from .serializer import ClassSerializer
from students.models import Student
from teachers.models import Teacher
from courses.models import Course
from classes.models import Class
from classPeriod.models import ClassPeriod



class StudentListView(APIView):
    def get(self, request, format=None):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
class TeacherListView(APIView):
    def get(self, request, format=None):
        teachers= Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
 
class CourseListView(APIView):
    def get(self, request, format=None):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
class ClassesListView(APIView):
    def get(self,request,format=None):
        classes =Class.objects.all()
        serializer= ClassSerializer(classes,many=true)
        return Response(serializer.data)
class ClassPeriodListView(APIView):
    def get(self,request,format=None):
    classperiods= ClassPeriod.objects.all()
    serializer= ClassPeriodSerializer(classperiods,many=True)
    return Response(serializer.data)
        
        

