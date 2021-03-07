from django import forms
from django.forms import ModelForm
from .models import *



class SendResponseForm(ModelForm):
    class Meta:
        model = Responses
        fields = '__all__'


class StudentLoginForm(ModelForm):
    class Meta:
        model = Student_Login
        fields = '__all__'


class StudentForm(ModelForm):
    class Meta:
        model = Responses
        fields = '__all__'


class TeacherLoginForm(ModelForm):
    class Meta:
        model = Teacher_Login
        fields = '__all__'


class TeacherForm(ModelForm):
    class Meta:
        model = Exercises
        fields = '__all__'


class UploadVideoForm(ModelForm):
    class Meta:
        model = Videos
        fields = '__all__'



#class ResultsForm(ModelForm):
 #   class Meta:
  #     model = Results
   #    fields = '__all__'



#class TeacherVideoForm(ModelForm):
 #   class Meta:
  #      model = Videos
   #     fields = '__all__'




class UploadExerciseForm(ModelForm):
    class Meta:
        model = Exercises
        fields = '__all__'
