from django.shortcuts import render, redirect
from .forms import UploadVideoForm
from django.http import HttpResponse
#from django.contrib import authenticate
#from .forms import UploadVideoForm
from .forms import *


def home(request):
    return render(request, "panel/home.html")


def TeacherLogin(request):
    form = TeacherLoginForm()
    context = {'form': form}
    return render(request, "panel/TeacherLogin.html", context)


def teacher(request):
    form = TeacherForm()
    context = {'form': form}
    return render(request, "panel/teacher.html", context)


def StudentLogin(request):
    form = StudentLoginForm()
    context = {'form': form}
    return render(request, "panel/StudentLogin.html", context)


def student(request):
    form = StudentForm()
    context = {'form': form}
    return render(request, "panel/student.html", context)


def student_video(request):
    form = Videos.objects.all()
    context = {'video': form}
    return render(request, 'panel/student_video_part.html', context)


def student_exercise(request):
    form = Exercises.objects.all()
    context = {'exercise': form}
    return render(request, 'panel/student_exercise_part.html', context)


def teacher_video(request):
    form = Videos.objects.all()
    context = {'video': form}
    return render(request, 'panel/teacher_video_part.html', context)


def teacher_exercise(request):
    form = Exercises.objects.all()
    context = {'exercise': form}
    return render(request, 'panel/teacher_exercise_part.html', context)


def sendResponse(request):
    form = SendResponseForm()
    if request.method == "POST":
        form = SendResponseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('file has been uploaded successfully.')
    context = {'form': form}
    return render(request, "panel/send_response.html", context)





def createVideo(request):
    form = UploadVideoForm()
    if request.method == "POST":
        form = UploadVideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('video has been uploaded successfully.')
    context = {'form': form}
    return render(request, "panel/create_video.html", context)

def videoDetail(request, video_id):
    vid = Videos.objects.get(id=video_id)
    context = {'video': vid}
    return render(request, 'panel/teacher_video_details.html', context)


#def resultDetail(request, result_id):
 #   res = Responses.objects.get(id=result_id)
  #  context = {'result': res}
   # return render(request, 'panel/result_detail.html', context)


def exercise(request):
    form = Exercises.objects.all()
    context = {'exercise': form}
    return render(request, "panel/exercise.html", context)








def createExercise(request):
    form = UploadExerciseForm()
    if request.method == "POST":
        form = UploadExerciseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('exercise has been uploaded successfully.')
    context = {'form': form}
    return render(request, "panel/create_exercise.html", context)



def response(request, score_id):
    form = Responses.objects.get(id=score_id)
    context = {'response': form}
    return render(request, "panel/response.html", context)







def results(request):
    res = Results.objects.all()
    context = {'result': res}
    return render(request, 'panel/results.html', context)



#def login(request):
 #   if request.method == "POST":
  #      username = request.POST["username"]
   #     password = request.POST["password"]
    #    identity = request.POST["identity"]
     #   user = authenticate()