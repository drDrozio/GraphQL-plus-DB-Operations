from django.shortcuts import render
from .models import Category, Quizzes, Question, Answer
from django.http import HttpResponse
import datetime
from blue.models import Blue

# Create your views here.
def databaseQueries(request):
	allQuizzes = Quizzes.objects.all()
	sportsQuizzes = allQuizzes.filter(category__name='Sports')
	sportsQuizzes=sportsQuizzes.exclude(date_created=datetime.date.today())

	categoryID = Category.objects.filter(name='Education')
	categoryID = categoryID.values_list('pk',flat=True)

	colors = Blue.objects.using('blue_db').all()

	context={'quizzes':sportsQuizzes , 'categoryID':categoryID , 'colors':colors}
	return render(request,'index.html',context)
