from django.db import models
from django.conf import settings


# Create your models here.
class SchoolRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    firstFirst = models.FloatField()
    firstSecond = models.FloatField()
    secondFirst = models.FloatField()
    secondSecond = models.FloatField()
    thirdFirst = models.FloatField()
    thirdSecond = models.FloatField()
    
    def __str__(self):
        return "평균: {}".format((self.firstFirst + self.firstSecond + self.secondFirst
                                + self.secondSecond + self.thirdFirst + self.thirdSecond) / 6)
    

class Test(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    month = models.IntegerField()
    koreanPoint = models.IntegerField()
    koreanGrade = models.IntegerField()
    mathPoint = models.IntegerField()
    mathGrade = models.IntegerField()
    englishPoint = models.IntegerField()
    englishGrade = models.IntegerField()
    tamguFirstName = models.CharField(max_length=20)
    tamguFirstGrade = models.IntegerField()
    tamguFirstPoint = models.IntegerField()
    tamguSecondName = models.CharField(max_length=20)
    tamguSecondGrade = models.IntegerField()
    tamguSecondPoint = models.IntegerField()
    foreignName = models.CharField(max_length=20)
    foreignGrade = models.IntegerField()
    foreignPoint = models.IntegerField()
    
    def __str__(self):
        return f"{self.month}"
    

class TargetUniv(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order = models.IntegerField()
    univ = models.CharField(max_length=30)
    major = models.CharField(max_length=30)
    applyType = models.CharField(max_length=30)
    
    def __str__(self):
        return self.univ + " " + self.major
    
# class StudyHour(models.Model):
#     content = models.CharField(max_length=140)
    
#     def __str__(self):
#         return self.content