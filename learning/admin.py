from django.contrib import admin
from .models import Entity, Semester,Department,Course,Quiz,Purchase,Instructor
# Register your models here.

@admin.register(Semester)
class SemesterRegister(admin.ModelAdmin):
    pass

@admin.register(Department)
class DepartmentRegister(admin.ModelAdmin):
    pass

@admin.register(Course)
class CourseRegister(admin.ModelAdmin):
    pass

@admin.register(Quiz)
class QuizRegister(admin.ModelAdmin):
    pass

@admin.register(Purchase)
class PurchaseRegister(admin.ModelAdmin):
    pass

@admin.register(Instructor)
class InstructorRegister(admin.ModelAdmin):
    pass

@admin.register(Entity)
class EntityRegister(admin.ModelAdmin):
    pass