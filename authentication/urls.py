from django.urls import path,include
from .views import home,getEntityDepartments,getDepartmentSemesters
app_name="authentication"
urlpatterns = [
    path('',home,name="home"),
    path('<pk>/<str:name>/departments/',getEntityDepartments,name="departments"),
    path('<pk>/<str:name>/semesters/',getDepartmentSemesters,name="semesters"),
]
