from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),

    path('video/create', views.createVideo, name='create_video'),

    path('video/<int:video_id>', views.videoDetail, name='teacher_video_details'),
    path('exercise/create', views.createExercise, name='create_exercise'),
    path('response/', views.response, name='responses'),
    path('response/send', views.sendResponse, name='send_response'),
    path('teacher/login', views.TeacherLogin, name='teacher_login'),
    path('student/login', views.StudentLogin, name='student_login'),
    path('student', views.student, name='student'),
    path('teacher', views.teacher, name='teacher'),
    path('teacher/video', views.teacher_video, name='teacher_video_part'),
    path('student/video', views.student_video, name='student_video_part'),
    path('student/exercise', views.student_exercise, name='student_exercise_part'),
    path('teacher/exercise', views.teacher_exercise, name='teacher_exercise_part'),
    path('results/', views.results, name='results'),


]

