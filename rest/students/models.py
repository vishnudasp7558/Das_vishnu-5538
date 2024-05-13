from django.db import models

class student(models.Model):
    name=models.ChareField(max_length=30)
    age=models.IntegerField(max_length=30)
    place=models.ChareField(max_length=30)

    def __str__(self):
        return self.name
# class student(models.Model):
#     name=models.CharField(max_length=30)
#     age=models.IntegerField()
#     place=models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.name
