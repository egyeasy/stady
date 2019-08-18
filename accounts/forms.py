from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from verified_email_field.forms import VerifiedEmailField


# class RegistrationForm(forms.ModelForm):
#     email = VerifiedEmailField(label='email', required=True)

    
class CustomUserCreationForm(UserCreationForm):
    # email = VerifiedEmailField(label='email', fieldsetup_id='registration-form-email', required=True)
    username = forms.CharField(label="이름")
    school = forms.CharField(label="학교")
    # grade = forms.CharField(label="학년")

    class Meta:
        model = get_user_model()
        # UserCreationForm에 있는 Meta 클래스의 fields를 그대로 쓰겠다.
        # fields = UserCreationForm.Meta.fields
        fields = ['email', 'username', 'school', 'grade']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_qs = get_user_model().objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("해당 이메일로 가입된 계정이 존재합니다.")
        return email
        
        
class CustomConsultCreationForm(UserCreationForm):
    # email = VerifiedEmailField(label='email', fieldsetup_id='registration-form-email', required=True)
    username = forms.CharField(label="이름")

    class Meta:
        model = get_user_model()
        # UserCreationForm에 있는 Meta 클래스의 fields를 그대로 쓰겠다.
        # fields = UserCreationForm.Meta.fields
        fields = ['email', 'username']