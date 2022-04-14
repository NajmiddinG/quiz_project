from django.shortcuts import render

# no-auth
def indexView(request):
    return render(request, 'no-auth/index.html')

def aboutView(request):
    return render(request, 'no-auth/about.html')

def contactView(request):
    return render(request, 'no-auth/contact.html')

def studentLoginView(request):
    return render(request, 'no-auth/student_login.html')

def studentRegisterView(request):
    return render(request, 'no-auth/student_register.html')

def tutorLoginView(request):
    return render(request, 'no-auth/tutor_login.html')

# auth-tutor
def addCourseTutorView(request):
    return render(request, 'auth-tutor/add_course.html')

def addQuestionTutorView(request):
    return render(request, 'auth-tutor/add_question.html')

def addTopicsTutorView(request):
    return render(request, 'auth-tutor/add_topics.html')

def addUsersTutorView(request):
    return render(request, 'auth-tutor/add_users.html')

def changePasswordTutorView(request):
    return render(request, 'auth-tutor/change_password.html')

def courseReportTutorView(request):
    return render(request, 'auth-tutor/course_report.html')

def dashboardTutorView(request):
    return render(request, 'auth-tutor/dashboard.html')

def myAccountTutorView(request):
    return render(request, 'auth-tutor/my_account.html')

def questionReportTutorView(request):
    return render(request, 'auth-tutor/question_report.html')

def resultReportTutorView(request):
    return render(request, 'auth-tutor/result_report.html')

def studentReportTutorView(request):
    return render(request, 'auth-tutor/student_report.html')

def topicReportTutorView(request):
    return render(request, 'auth-tutor/topic_report.html')

def tutorReportTutorView(request):
    return render(request, 'auth-tutor/tutor_report.html')

def dashboardTutorView(request):
    return render(request, 'auth-tutor/dashboard.html')

def dashboardTutorView(request):
    return render(request, 'auth-tutor/dashboard.html')

# auth-student