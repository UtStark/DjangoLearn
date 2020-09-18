from django.http import HttpResponse
from .models import Attendance

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def physics_marks(request,enrollno):
    question = Attendance.objects.get(enrollno=enrollno)
    q=question.physics
    return HttpResponse("your marks are %s" % q )