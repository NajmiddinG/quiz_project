from django.urls import path
from . import views

urlpatterns = [
    # no-auth
    path('', views.indexView, name='indexView'),
    path('about', views.aboutView, name='aboutView'),
    path('contact', views.contactView, name='contactView'),
    path('student-login', views.studentLoginView, name='studentLoginView'),
    path('student-register', views.studentRegisterView, name='studentRegisterView'),
    path('tutor-login/', views.tutorLoginView, name='tutorLoginView'),
    # auth tutor
    path('add-course-tutor', views.addCourseTutorView, name='addCourseTutor'),
    path('add-question-tutor', views.addQuestionTutorView, name='addQuestionTutor'),
    path('add-topics-tutor', views.addTopicsTutorView, name='addTopicsTutor'),
    path('add-users-tutor', views.addUsersTutorView, name='addUsersTutor'),
    path('change-password-tutor', views.changePasswordTutorView, name='changePasswordTutor'),
    path('course-report-tutor', views.courseReportTutorView, name='courseReportTutor'),
    path('dashboard-tutor', views.dashboardTutorView, name='dashboardTutor'),
    path('my-account-tutor', views.myAccountTutorView, name='myAccountTutor'),
    path('question-report-tutor', views.questionReportTutorView, name='questionReportTutor'),
    path('result-report-tutor', views.resultReportTutorView, name='resultReportTutor'),
    path('student-report-tutor', views.studentReportTutorView, name='studentReportTutor'),
    path('topic-report-tutor', views.topicReportTutorView, name='topicReportTutor'),
    path('tutor-report-tutor', views.tutorReportTutorView, name='tutorReportTutor'),
]