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


class Record(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='record/')


class Test(models.Model):
    YEAR_GROUP = ((2011, '2011년'), (2012, '2012년'), (2013, '2013년'), (2014, '2014년'), (2015, '2015년'),
                  (2016, '2016년'), (2017, '2017년'), (2018, '2018년'), (2019, '2019년'),)
    MONTH_GROUP = ((1, '1월'), (2, '2월'), (3, '3월'), (4, '4월'), (5, '5월'), (6, '6월'),
                  (7, '7월'), (8, '8월'), (9, '9월'), (10, '10월'), (11, '11월'), (12, '12월'))
    GRADE_GROUP = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9))
    TAMGU_GROUP = (("생활과 윤리","생활과 윤리"),("윤리와 사상","윤리와 사상"), ("한국지리", "한국지리"), ("세계지리","세계지리"),
                ("동아시아사", "동아시아사"), ("세계사","세계사"), ("법과 정치", "법과 정치"), ("경제", "경제"), ("사회문화","사회문화"),
                ("물리 I", "물리 I"), ("물리 II", "물리 II"), ("화학 I", "화학 I"), ("화학 II", "화학 II"),
                 ("생물 I", "생물 I"), ("생물 II", "생물 II"), ("지구과학 I", "지구과학 I"), ("지구과학 II", "지구과학 II"))
    FOREIGN_GROUP = (("중국어", "중국어"), ("일본어", "일본어"), ("독일어", "독일어"), ("프랑스어", "프랑스어"), ("스페인어", "스페인어"),
                     ("러시아어", "러시아어"), ("아랍어", "아랍어"), ("베트남어", "베트남어"), ("한문", "한문"),)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    year = models.IntegerField(choices=YEAR_GROUP, verbose_name="연도", blank=True)
    month = models.IntegerField(choices=MONTH_GROUP, verbose_name="월", blank=True)
    koreanPoint = models.IntegerField(blank=True)
    koreanGrade = models.IntegerField(choices=GRADE_GROUP, blank=True)
    mathPoint = models.IntegerField(blank=True)
    mathGrade = models.IntegerField(choices=GRADE_GROUP, blank=True)
    englishPoint = models.IntegerField(blank=True)
    englishGrade = models.IntegerField(choices=GRADE_GROUP, blank=True)
    tamguFirstName = models.CharField(max_length=20, choices=TAMGU_GROUP, verbose_name="탐구1", blank=True)
    tamguFirstGrade = models.IntegerField(choices=GRADE_GROUP, blank=True)
    tamguFirstPoint = models.IntegerField(blank=True)
    tamguSecondName = models.CharField(max_length=20, choices=TAMGU_GROUP, verbose_name="탐구2", blank=True)
    tamguSecondGrade = models.IntegerField(choices=GRADE_GROUP, blank=True)
    tamguSecondPoint = models.IntegerField(blank=True)
    foreignName = models.CharField(max_length=20, choices=FOREIGN_GROUP, verbose_name="제2외국어", blank=True)
    foreignGrade = models.IntegerField(choices=GRADE_GROUP, blank=True)
    foreignPoint = models.IntegerField(blank=True)
    
    def __str__(self):
        return f"{self.year} {self.month}, {self.user}"
    

class TargetUniv(models.Model):
    ORDER_GROUP = ((1, 1), (2, 2), (3, 3))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order = models.IntegerField(choices=ORDER_GROUP, verbose_name="지망 순위", blank=True)
    univ = models.CharField(max_length=30, blank=True)
    major = models.CharField(max_length=30, blank=True)
    applyType = models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        return self.univ + " " + self.major + ", " + str(self.user)
    
# class StudyHour(models.Model):
#     content = models.CharField(max_length=140)
    
#     def __str__(self):
#         return self.content


class Question(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    