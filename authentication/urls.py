from django.urls import path,include
from .views import home,getEntityDepartments,getDepartmentSemesters,getSemesterCourses,getCourseLessons
app_name="authentication"
urlpatterns = [
    path('',home,name="home"),
    path('<pk>/<str:name>/departments/',getEntityDepartments,name="departments"),
    path('<pk>/<str:name>/semesters/',getDepartmentSemesters,name="semesters"),
    path('semester/<pk>/<str:period>/courses/',getSemesterCourses,name="courses"),
    path('course/<pk>/<str:name>/lessons/',getCourseLessons,name="lessons"),

]
