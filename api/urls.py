from django.urls import path
from .views import StudentListView
from .views import TeacherListView
from .views import CourseListView
from .views import ClassesListView
from .views import ClassPeriodListView

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student_list_view'),
    path('teachers/', TeacherListView.as_view(), name='teachers_list_view'),
    path('courses/', CourseListView.as_view(), name='courses_list_view'),
    path('classes/', ClassesListView.as_view(), name='classes_list_view'),
    path('classPeriod/', ClassPeriodListView.as_view(), name='classperiods_list_view'),
    
]
