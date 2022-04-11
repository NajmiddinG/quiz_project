from django.db import models

# General
class About(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    phone = models.CharField(max_length=50)
    message = models.TextField(max_length=1000)
    join_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.name

# Tutor
class Tutor(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    login_id = models.CharField(max_length=70)
    pasword = models.CharField(max_length=70)
    email = models.EmailField(max_length=70, blank=True, null=True)
    phone = models.CharField(max_length=70, blank=True, null=True)
    birthday = models.DateField(max_length=70, blank=True, null=True)
    adres_1 = models.TextField(max_length=370, blank=True, null=True)
    adres_2 = models.TextField(max_length=370, blank=True, null=True)
    city = models.TextField(max_length=370, blank=True, null=True)
    state = models.TextField(max_length=370, blank=True, null=True)
    country = models.TextField(max_length=370, blank=True, null=True)
    picture = models.ImageField(upload_to='media/', blank=True, null=True)
    show_entries = models.IntegerField(default=10)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.first_name

class Course(models.Model):
    course_name = models.CharField(unique=True, max_length=50)
    description = models.TextField(max_length=1000, blank=True, null=True)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.course_name

class Topic(models.Model):
    levels = (
        ('l', 'Low'),
        ('m', 'Medium'),
        ('h', 'High'),
    )
    select_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    topic_name = models.CharField(max_length=100)
    select_level = models.CharField(max_length=1, choices=levels, default='m')
    description = models.TextField(max_length=1000, blank=True, null=True)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.topic_name

class AddQuestion(models.Model):
    select_course = models.ForeignKey(Topic, on_delete=models.CASCADE)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.select_course.select_course.course_name

class Question(models.Model):
    connected = models.ForeignKey(AddQuestion, on_delete=models.CASCADE)
    full_question = models.TextField(max_length=700)
    option1 = models.TextField(max_length=300)
    option2 = models.TextField(max_length=300)
    option3 = models.TextField(max_length=300)
    option4 = models.TextField(max_length=300)
    answer = models.TextField(max_length=300)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.full_question

# Student
class Student(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    login_id = models.CharField(max_length=70)
    pasword = models.CharField(max_length=70)
    email = models.EmailField(max_length=70, blank=True, null=True)
    choose = (
        ('m', 'Male'),
        ('f','Fmale')
    )
    gender = models.CharField(max_length=1,choices=choose, default='m')
    phone = models.CharField(max_length=70, blank=True, null=True)
    birthday = models.DateField(max_length=70, blank=True, null=True)
    adres_1 = models.TextField(max_length=370, blank=True, null=True)
    adres_2 = models.TextField(max_length=370, blank=True, null=True)
    city = models.TextField(max_length=370, blank=True, null=True)
    state = models.TextField(max_length=370, blank=True, null=True)
    country = models.TextField(max_length=370, blank=True, null=True)
    picture = models.ImageField(upload_to='media/', blank=True, null=True)
    show_entries = models.IntegerField(default=10)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.first_name

class TopicDetail(models.Model):
    topic_name = models.ForeignKey(Topic, on_delete=models.CASCADE)
    result = models.CharField(max_length=100,default='')
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.topic_name.topic_name

class MyResult(models.Model):
    username = models.ForeignKey(Student, on_delete=models.CASCADE)
    topic_detail = models.ForeignKey(TopicDetail, on_delete=models.CASCADE)
    marks = models.CharField(max_length=30)
    join_date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.username.first_name