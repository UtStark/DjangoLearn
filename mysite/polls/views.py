from django.http import HttpResponse
from .models import Attendance
from django.shortcuts import get_object_or_404, render

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def physics_marks(request,enrollno):

    question = get_object_or_404(Attendance, enrollno=enrollno)
    q=question.physics
    return HttpResponse("your  attendance is %s" % q )

def physics_marks_update(request,enrollno):

    question = get_object_or_404(Attendance, enrollno=enrollno)
    q=question.physics
    question.physics=q+1
    question.save()
    return HttpResponse(status=204)



