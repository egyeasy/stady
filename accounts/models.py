from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.conf import settings
from verified_email_field.models import VerifiedEmailField
from simple_email_confirmation.models import SimpleEmailConfirmationUserMixin


# Create your models here.
class User(AbstractUser):
    # email = VerifiedEmailField('e-mail', fieldsetup_id='user-email')
    GRADE_GROUP = ((1, '1학년'), (2, '2학년'), (3, '3학년'))
    email = models.EmailField(unique=True, verbose_name='이메일')
    username = models.CharField(max_length=50, blank=True, verbose_name="이름")
    school = models.CharField(max_length=30, blank=True, verbose_name="학교")
    grade = models.IntegerField(choices=GRADE_GROUP, null=True, verbose_name="학년")
    is_payed = models.BooleanField(null=True, verbose_name="결제 여부")
    is_feedbacked = models.BooleanField(null=True, verbose_name="피드백 여부")
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    


class UserManager(BaseUserManager):
    def create_superuser(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not username:
            raise ValueError("User must have a username")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.username = username
        user.set_password(password)
        user.admin = True
        user.staff = True
        user.save(using=self._db)
        return user