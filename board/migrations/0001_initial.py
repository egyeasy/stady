# Generated by Django 2.1.8 on 2019-08-15 05:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=10000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='record/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstFirst', models.FloatField()),
                ('firstSecond', models.FloatField()),
                ('secondFirst', models.FloatField()),
                ('secondSecond', models.FloatField()),
                ('thirdFirst', models.FloatField()),
                ('thirdSecond', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TargetUniv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3)], verbose_name='지망 순위')),
                ('univ', models.CharField(blank=True, max_length=30)),
                ('major', models.CharField(blank=True, max_length=30)),
                ('applyType', models.CharField(blank=True, max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(blank=True, choices=[(2011, '2011년'), (2012, '2012년'), (2013, '2013년'), (2014, '2014년'), (2015, '2015년'), (2016, '2016년'), (2017, '2017년'), (2018, '2018년'), (2019, '2019년')], verbose_name='연도')),
                ('month', models.IntegerField(blank=True, choices=[(1, '1월'), (2, '2월'), (3, '3월'), (4, '4월'), (5, '5월'), (6, '6월'), (7, '7월'), (8, '8월'), (9, '9월'), (10, '10월'), (11, '11월'), (12, '12월')], verbose_name='월')),
                ('koreanPoint', models.IntegerField(blank=True)),
                ('koreanGrade', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)])),
                ('mathPoint', models.IntegerField(blank=True)),
                ('mathGrade', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)])),
                ('englishPoint', models.IntegerField(blank=True)),
                ('englishGrade', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)])),
                ('tamguFirstName', models.CharField(blank=True, choices=[('생활과 윤리', '생활과 윤리'), ('윤리와 사상', '윤리와 사상'), ('한국지리', '한국지리'), ('세계지리', '세계지리'), ('동아시아사', '동아시아사'), ('세계사', '세계사'), ('법과 정치', '법과 정치'), ('경제', '경제'), ('사회문화', '사회문화'), ('물리 I', '물리 I'), ('물리 II', '물리 II'), ('화학 I', '화학 I'), ('화학 II', '화학 II'), ('생물 I', '생물 I'), ('생물 II', '생물 II'), ('지구과학 I', '지구과학 I'), ('지구과학 II', '지구과학 II')], max_length=20, verbose_name='탐구1')),
                ('tamguFirstGrade', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)])),
                ('tamguFirstPoint', models.IntegerField(blank=True)),
                ('tamguSecondName', models.CharField(blank=True, choices=[('생활과 윤리', '생활과 윤리'), ('윤리와 사상', '윤리와 사상'), ('한국지리', '한국지리'), ('세계지리', '세계지리'), ('동아시아사', '동아시아사'), ('세계사', '세계사'), ('법과 정치', '법과 정치'), ('경제', '경제'), ('사회문화', '사회문화'), ('물리 I', '물리 I'), ('물리 II', '물리 II'), ('화학 I', '화학 I'), ('화학 II', '화학 II'), ('생물 I', '생물 I'), ('생물 II', '생물 II'), ('지구과학 I', '지구과학 I'), ('지구과학 II', '지구과학 II')], max_length=20, verbose_name='탐구2')),
                ('tamguSecondGrade', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)])),
                ('tamguSecondPoint', models.IntegerField(blank=True)),
                ('foreignName', models.CharField(blank=True, choices=[('중국어', '중국어'), ('일본어', '일본어'), ('독일어', '독일어'), ('프랑스어', '프랑스어'), ('스페인어', '스페인어'), ('러시아어', '러시아어'), ('아랍어', '아랍어'), ('베트남어', '베트남어'), ('한문', '한문')], max_length=20, verbose_name='제2외국어')),
                ('foreignGrade', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)])),
                ('foreignPoint', models.IntegerField(blank=True)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
