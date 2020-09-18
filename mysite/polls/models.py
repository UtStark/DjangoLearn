from django.db import models

class Attendance(models.Model):

    name=models.CharField(max_length=100)
    enrollno=models.IntegerField(default=0)
    physics=models.IntegerField(default=0)
    chemistry=models.IntegerField(default=0)
    math=models.IntegerField(default=0)

    def __str__(self):
        return self.name

