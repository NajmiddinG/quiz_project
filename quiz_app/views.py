from django.shortcuts import render

# no-auth
def indexView(request):
    return render(request, 'no-auth/index.html', {'user_cookie': request.COOKIES})

def aboutView(request):
    return render(request, 'no-auth/about.html', {'user_cookie': request.COOKIES})

def contactView(request):
    return render(request, 'no-auth/contact.html', {'user_cookie': request.COOKIES})

def studentLoginView(request):
    return render(request, 'no-auth/student_login.html', {'user_cookie': request.COOKIES})

def studentRegisterView(request):
    return render(request, 'no-auth/student_register.html', {'user_cookie': request.COOKIES})

def tutorLoginView(request):
    return render(request, 'no-auth/tutor_login.html', {'user_cookie': request.COOKIES})

def LogoutView(request):
    return render(request, 'no-auth/index.html', {'user_cookie': request.COOKIES})

# auth-tutor
def addCourseTutorView(request):
    return render(request, 'auth-tutor/add_course.html', {'user_cookie': request.COOKIES})

def addQuestionTutorView(request):
    return render(request, 'auth-tutor/add_question.html', {'user_cookie': request.COOKIES})

def addTopicsTutorView(request):
    return render(request, 'auth-tutor/add_topics.html', {'user_cookie': request.COOKIES})

def addUsersTutorView(request):
    return render(request, 'auth-tutor/add_users.html', {'user_cookie': request.COOKIES})

def changePasswordTutorView(request):
    return render(request, 'auth-tutor/change_password.html', {'user_cookie': request.COOKIES})

def courseReportTutorView(request):
    return render(request, 'auth-tutor/course_report.html', {'user_cookie': request.COOKIES})

def dashboardTutorView(request):
    return render(request, 'auth-tutor/dashboard.html', {'user_cookie': request.COOKIES})

def myAccountTutorView(request):
    return render(request, 'auth-tutor/my_account.html', {'user_cookie': request.COOKIES})

def questionReportTutorView(request):
    return render(request, 'auth-tutor/question_report.html', {'user_cookie': request.COOKIES})

def resultReportTutorView(request):
    return render(request, 'auth-tutor/result_report.html', {'user_cookie': request.COOKIES})

def studentReportTutorView(request):
    return render(request, 'auth-tutor/student_report.html', {'user_cookie': request.COOKIES})

def topicReportTutorView(request):
    return render(request, 'auth-tutor/topic_report.html', {'user_cookie': request.COOKIES})

def tutorReportTutorView(request):
    return render(request, 'auth-tutor/tutor_report.html', {'user_cookie': request.COOKIES})

def dashboardTutorView(request):
    return render(request, 'auth-tutor/dashboard.html', {'user_cookie': request.COOKIES})

def dashboardTutorView(request):
    return render(request, 'auth-tutor/dashboard.html', {'user_cookie': request.COOKIES})

# auth-student


def dashboardStudentView(request):
    return render(request, 'auth-student/dashboard.html', {'user_cookie': request.COOKIES})

def courseListStudentView(request):
    return render(request, 'auth-student/course_list.html', {'user_cookie': request.COOKIES})

def myAccountStudentView(request):
    return render(request, 'auth-student/my_account.html', {'user_cookie': request.COOKIES})

def myResultStudentView(request):
    return render(request, 'auth-student/my_result.html', {'user_cookie': request.COOKIES})

def changePasswordStudentView(request):
    return render(request, 'auth-student/change_password.html', {'user_cookie': request.COOKIES})