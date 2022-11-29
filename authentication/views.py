from django.shortcuts import render
from learning.models import Entity,Department,Semester
from django.contrib.auth.decorators import login_required,user_passes_test
# Create your views here.
def home(request):
    entity=Entity.objects.all()
    context={
        'entities':entity  
    }
    return render(request,"authentication/site_home.html",context)

@login_required
def getEntityDepartments(request,pk,name):
    entity = Entity.objects.get(pk=pk,name=name)
    semesters = entity.semesters.all()
    departments = entity.departments.all()
    context={
        'entity':entity,
        'departments':departments,
        'semesters':semesters
    }
    return render(request,"Authentication/departments.html",context)

def getDepartmentSemesters(request,pk,name):
    department = Department.objects.get(pk=pk,name=name)
    semesters = department.semesters.all()
    context={
        'department':department,
        'semesters':semesters
    }
    return render(request,"authentication/semesters.html",context)

def getSemesterCourses(request,pk,name):
    semester = Semester.objects.get(pk=pk,name=name)
    courses = semester.courses.all()
    context={
        'semester':semester,
        'courses':courses
    }
    return render(request,"authentication/courses.html",context)

