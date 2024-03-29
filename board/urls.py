from django.urls import path
from . import views

app_name = "board"

urlpatterns = [
    path('', views.index, name="index"),
    path('fillout-school/', views.fillout_school, name="fillout_school"),
    path('fillout-record/', views.fillout_record, name="fillout_record"),
	# path('fillout-test', views.fillout_test, name="fillout_test"),
	path('fillout-test/', views.TestFormView.as_view(), name="fillout_test"),
    # path('fillout-target/', views.fillout_target, name="fillout_target"),
    path('fillout-target/', views.TargetUnivFormView.as_view(), name="fillout_target"),
    path('fillout-question/', views.fillout_question, name="fillout_question"),
    path('overview/', views.overview, name="overview"),
    path('register/', views.register, name="register"),
]
