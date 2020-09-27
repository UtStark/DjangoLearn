from django.urls import path

from . import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:enrollno>/physics', views.physics_marks , name='physics_marks'),
    path('<int:enrollno>/physics/update', views.physics_marks_update, name='physics_marks_update'),
]