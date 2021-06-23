from django.shortcuts import render
from .models import Category, Quizzes, Question, Answer
from django.http import HttpResponse
import datetime

# Create your views here.
def databaseQueries(request):
	allQuizzes = Quizzes.objects.all()
	sportsQuizzes = allQuizzes.filter(category__name='Sports')
	sportsQuizzes=sportsQuizzes.exclude(date_created=datetime.date.today())
	context={'quizzes':sportsQuizzes}
	return render(request,'index.html',context)
