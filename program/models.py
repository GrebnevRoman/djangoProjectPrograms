from django.db import models


# Create your models here.
# class Mod(models.Model):
#   name = models.TextField()


class Departments(models.Model):
    Code = models.CharField(max_length=30)
    Name = models.CharField(max_length=30)

    def __str__(self):
        return self.Name


class Specialty(models.Model):
    Name = models.CharField(max_length=30)
    Code = models.IntegerField()

    def __str__(self):
        return self.Name


class Programs(models.Model):
    Name = models.CharField(max_length=30)
    Specialty = models.ManyToManyField(Specialty)
    Dep = models.ForeignKey('Departments', on_delete=models.PROTECT)
    General_hours = models.IntegerField()
    Code = models.IntegerField()
    Classroom_hours = models.IntegerField()
    Registration_date = models.DateTimeField(auto_now_add=True)
    Type = models.CharField(max_length=20)

    def __str__(self):
        return self.Name


class Direction(models.Model):
    Name = models.CharField(max_length=30)
    Code = models.IntegerField()
    Spec = models.ForeignKey('Specialty', on_delete=models.PROTECT)

    def __str__(self):
        return self.Name


