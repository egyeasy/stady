# stady
교육 컨설팅 서비스 프로젝트

## heroku url
https://desolate-bastion-17607.herokuapp.com/

## runserver
url : https://stady-bften.run.goorm.io/

how to runserver : `python manage.py runserver 0.0.0.0:8080`


## reference
### 여러 instance를 동시에 넘기기
https://stackoverflow.com/questions/4902333/django-how-to-make-a-form-with-custom-templating

여러 form 추가/제거하기(django dynamic formset)
https://github.com/elo80ka/django-dynamic-formset/blob/master/src/jquery.formset.js

(2019.8.15) inlineformset factory - post와 update를 동시에
https://stackoverflow.com/questions/1988968/django-formset-how-to-update-an-object

### 권한 관리
https://heiswed.tistory.com/entry/%EC%9E%A5%EA%B3%A0Django-%EA%B0%9C%EB%B0%9C-%EA%B6%8C%ED%95%9Cpermission-%ED%99%94%EB%A9%B4-%EA%B4%80%EB%A6%AC

그냥 login app에서 링크 하나 파서 같은 url로 보낼 것. request url 확인은
https://stackoverflow.com/questions/2882490/how-to-get-the-current-url-within-a-django-template

### 이메일 인증
https://stackoverflow.com/questions/24935271/django-custom-user-email-account-verification

위에꺼 안돼서 밑에걸로 넣어놓음(인증 기능은 없는 상태)
https://pypi.org/project/django-simple-email-confirmation/


### heroku
Collectstatic 관련 이슈 - collectstatic을 쓰지 않는 쪽으로 해결된 듯
https://stackoverflow.com/questions/36665889/collectstatic-error-while-deploying-django-app-to-heroku/36676953

#### heroku django 관련 공식 문서
https://devcenter.heroku.com/articles/django-assets

#### django collectstatic 관련 공식 문서
https://docs.djangoproject.com/en/2.1/howto/static-files/#deployment

#### ROOT path 설정하기(500 error when DEBUG=True)
https://stackoverflow.com/questions/53246297/django-core-exceptions-suspiciousfileoperation-the-joined-path-is-located-outsi

위에거 안돼서 heroku 공식 문서 참조
https://devcenter.heroku.com/articles/django-assets

#### log
https://stackoverflow.com/questions/18920428/django-logging-on-heroku/20983546#20983546

#### heroku를 위한 settings.py
static 폴더의 이름을 staticfiles로 변경
```python
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'static'),
)

STATIC_URL = '/static/'

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 절대경로로 나타내기 때문에 os.path.join 사용
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# 파일 주소에 접미사를 만들어줌
MEDIA_URL = '/media/'


# django-heroku setting
django_heroku.settings(locals())

# django-heroku whitenoise setting
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```
