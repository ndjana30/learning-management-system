from django.db import models
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField
from django.urls import reverse

# Create your models here.
class Entity(models.Model):
    name=models.CharField(max_length=255,blank=False,null=False)
    location = PlainLocationField(based_fields=['city'], zoom=7)

    def get_absolute_url(self):
        return reverse("authentication:departments", args=[self.pk,self.name])

    def __str__(self):
        return self.name

class Department(models.Model):
    selections = (('ICT','ict'),('BMS','bms'))
    entity = models.ForeignKey(Entity,related_name="departments",on_delete=models.CASCADE,null=True,blank=True)
    ICT=(('ICT','ict'))
    name = models.CharField(choices=selections,default=ICT,blank=False,null=False, max_length=255)

    def get_absolute_url(self):
        return reverse("authentication:semesters", args=[self.pk,self.name])


    def __str__(self):
        return f'{self.name} for {self.entity}' 

class Semester(models.Model):
    Fall=('FALL','fall')
    seasons = (('FALL','fall'),('SPRING','spring'),('SUMMER','summer'))
    entity = models.ForeignKey(Entity,related_name="semesters",on_delete=models.CASCADE,null=True,blank=True)
    period = models.CharField(choices=seasons, default=Fall, blank=False,null=False, max_length=255)
    datentime = models.DateTimeField(auto_now = True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name="semesters",null=True,blank=True)

    def get_absolute_url(self):
        return reverse("authentication:semesters",args=[self.pk,self.period])

    def __str__(self):
        return f'{self.period} Semester for {self.entity}'


class Instructor(models.Model):
    onTheRun = models.BooleanField(default=False)
    name = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class Course(models.Model):
    name=models.CharField(max_length = 255, blank=False, null=False)
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE,related_name='courses')
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    credits = models.PositiveIntegerField(default=3, null=False,blank=False)
    instructor = models.ForeignKey(Instructor,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now = True)
    price = models.PositiveIntegerField(default = 0, blank = False, null=False)
    free = models.BooleanField(default= False, blank=False,null=False)
    level = models.PositiveIntegerField(blank=True,null=True)

    def get_absolute_url(self):
        return reverse("authentication:courses",args=[self.name,self.pk])

    def __str__(self):
        return self.name

class Lesson(models.Model):
    name = models.CharField(max_length=250,blank=True,null=True)
    slug = models.SlugField(null=True,blank=True)
    lesson_file = models.FileField(upload_to="lessons/",blank=True,null=True)
    lesson_file1 = models.FileField(upload_to="lessons/",blank=True,null=True)
    lesson_file2 = models.FileField(upload_to="lessons/",blank=True,null=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="lessons")
    free = models.BooleanField(default= False, blank=False,null=False)
    price = models.PositiveIntegerField(default = 0, blank = False, null=False)

    def get_absolute_url(self):
        return reverse("authentication:lessons",args=[self.pk,self.name])

    def __str__(self):
        return f'{self.name} for {self.course}'

class Quiz(models.Model):
    course = models.ForeignKey(Course,related_name='quizes',on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False,blank=False)
    created = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

class Question(models.Model):
    sentence = models.TextField(max_length=255)
    quiz = models.ForeignKey(Quiz,related_name='questions',on_delete=models.CASCADE)
    a =  models.TextField(max_length=255)
    b =  models.TextField(max_length=255)
    c =  models.TextField(max_length=255)
    d =  models.TextField(max_length=255)
    ans = models.TextField(max_length=250)
    mark = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.sentence

class Purchase(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='purchased')
    purchaser = models.ForeignKey(User,on_delete=models.CASCADE,related_name='purchases')

    def __str__(self):
        return f' {self.course} purchased by \t {self.purchaser}'

class result(models.Model):
    student = models.ForeignKey(User,related_name='result',on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz,related_name="results",on_delete=models.CASCADE)
    total = models.PositiveIntegerField(default=0)
