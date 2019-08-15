from django.urls import path
from . import views

app_name = "manage"

urlpatterns = [
    path('students/', views.student_list, name="student_list"),
    path('students/<str:student_email>', views.overview, name="overview"),
    # path('fillout-record/', views.fillout_record, name="fillout_record"),
	# path('fillout-test', views.fillout_test, name="fillout_test"),
	# path('fillout-test/', views.TestFormView.as_view(), name="fillout_test"),
    # path('fillout-target/', views.fillout_target, name="fillout_target"),
    # path('fillout-target/', views.TargetUnivFormView.as_view(), name="fillout_target"),
    # path('fillout-question/', views.fillout_question, name="fillout_question"),
    # path('overview/', views.overview, name="overview"),
]
