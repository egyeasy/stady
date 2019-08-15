from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from verified_email_field.models import VerifiedEmailField
from simple_email_confirmation.models import SimpleEmailConfirmationUserMixin


# Create your models here.
class User(SimpleEmailConfirmationUserMixin, AbstractUser):
    # email = VerifiedEmailField('e-mail', fieldsetup_id='user-email')
    email = models.EmailField(unique=True, verbose_name='이메일')
    username = models.CharField(max_length=50, blank=True, verbose_name="이름")
    school = models.CharField(max_length=30, blank=True, verbose_name="학교")
    grade = models.IntegerField(null=True, verbose_name="학년")
    is_payed = models.BooleanField(null=True, verbose_name="결제 여부")
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []