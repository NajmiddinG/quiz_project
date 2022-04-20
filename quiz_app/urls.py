from django.urls import path
from . import views

urlpatterns = [
    # no-auth
    path('', views.indexView, name='index'),
    path('about/', views.aboutView, name='about'),
    path('contact/', views.contactView, name='contact'),
    path('student-login/', views.studentLoginView, name='studentLogin'),
    path('student-register/', views.studentRegisterView, name='studentRegister'),
    path('tutor-login/', views.tutorLoginView, name='tutorLogin'),
    path('logout/', views.LogoutView, name='logout'),
    # auth tutor
    path('add-course-tutor/', views.addCourseTutorView, name='addCourseTutor'),
    path('add-question-tutor/', views.addQuestionTutorView, name='addQuestionTutor'),
    path('add-topics-tutor/', views.addTopicsTutorView, name='addTopicsTutor'),
    path('add-users-tutor/', views.addUsersTutorView, name='addUsersTutor'),
    path('change-password-tutor/', views.changePasswordTutorView, name='changePasswordTutor'),
    path('course-report-tutor/', views.courseReportTutorView, name='courseReportTutor'),
    path('dashboard-tutor/', views.dashboardTutorView, name='dashboardTutor'),
    path('my-account-tutor/', views.myAccountTutorView, name='myAccountTutor'),
    path('question-report-tutor/', views.questionReportTutorView, name='questionReportTutor'),
    path('result-report-tutor/', views.resultReportTutorView, name='resultReportTutor'),
    path('student-report-tutor/', views.studentReportTutorView, name='studentReportTutor'),
    path('topic-report-tutor/', views.topicReportTutorView, name='topicReportTutor'),
    path('tutor-report-tutor/', views.tutorReportTutorView, name='tutorReportTutor'),
    # auth student
    path('changePasswordStudentView/', views.changePasswordStudentView, name='changePasswordStudent'),
    path('courseListStudentView/', views.courseListStudentView, name='courseListStudent'),
    path('dashboardStudentView/', views.dashboardStudentView, name='dashboardStudent'),
    path('myAccountStudentView/', views.myAccountStudentView, name='myAccountStudent'),
    path('myResultStudentView/', views.myResultStudentView, name='myResultStudent'),
    
]