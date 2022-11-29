from django.shortcuts import render
from learning.models import (
    Entity,
    Department,
    Semester,
    Course,
    Quiz,
    Question,
    Purchase)
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

def getSemesterCourses(request,pk,period):
    semester = Semester.objects.get(pk=pk,period=period)
    courses = semester.courses.all()
    context={
        'semester':semester,
        'courses':courses,
    }
    return render(request,"authentication/courses.html",context)

def getCourseLessons(request,pk,name):
    course = Course.objects.get(pk=pk,name=name)
    lessons = course.lessons.all()
    context={
        'course':course,
        'lessons':lessons,
    }
    return render(request,'authentication/lessons.html',context)

def addCourseQuiz(request,pk,name):
    course = Course.objects.get(pk=pk,name=name)
    quiz = Quiz.objects.all()
    quiz.course=course
    quiz.name = request.POST.get('name')
    quiz.save()
    context={
        'course':course,
        'quiz':quiz,
    }
    return render(request,'authentication/add_quiz.html',context)
    
def addQuizQuestions(request,pk,name):
    quiz = Quiz.objects.get(pk=pk,name=name)
    question = Question.objects.all()
    question.quiz=quiz
    question.ans=request.POST.get('ans')
    question.a=request.POST.get('a')
    question.b=request.POST.get('b')
    question.c=request.POST.get('c')
    question.d=request.POST.get('d')
    question.mark = 1
    question.save()

def PurchaseCourse(request,pk,name):
    course = Course.objects.get(pk=pk,name=name)
    purchaser = request.user
    purchase=Purchase.objects.all()
    purchase.course=course
    purchase.purchaser=purchaser
    purchase.save()

