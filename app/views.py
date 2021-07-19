from django.shortcuts import render
from .models import Category, Quizzes, Question, Answer
from django.http import HttpResponse
import datetime
from blue.models import Blue, Movie , Character, Framework, Language
from django.db.models import Q

# Create your views here.
def databaseQueries(request):
	allQuizzes = Quizzes.objects.all()
	sportsQuizzes = allQuizzes.filter(category__name='Sports')
	sportsQuizzes=sportsQuizzes.exclude(date_created=datetime.date.today())

	categoryID = Category.objects.filter(name='Education')
	categoryID = categoryID.values_list('pk',flat=True)

	colors = Blue.objects.using('blue_db').all()

	# cap = Character.objects.all()
	# cap = cap.filter(name='Captain America')
	# print(cap[0].name)
	# print(cap[0].movies)

	# chars=Character.objects.filter(movies__title='Avengers')
	# print("Characters in Avengers Movie :- ")
	# for char in chars:
	# 	print(char)
	# print("Movies that feature Hulk :- ")
	# movchars = Movie.objects.filter(character__name='Hulk')
	# for movchar in movchars:
	# 	print(movchar)

	# print("Characters in Captain America Civil War :-")
	# civilwar = Movie.objects.get(title='Captain America Civil War')
	# civilwarchars = civilwar.character_set.all()
	# for civilwarchar in civilwarchars:
	# 	print(civilwarchar)

	# # Using select_related
	# quiz_cats = Quizzes.objects.all().select_related('category') 
	# for quiz_cat in quiz_cats:
	# 	print(quiz_cat.title, quiz_cat.category.name)

	# # ManytoMany Fields using set
	# movies = Movie.objects.all()
	# for movie in movies:
	# 	print(movie," : ")
	# 	print(movie.character_set.all())
	# # Using prefetch_related
	# movies = Movie.objects.all().prefetch_related('character_set')
	# for movie in movies:
	# 	print(movie," : ")
	# 	for chars in movie.character_set.all():
	# 		print(chars,end="  ")
	# 	print()
	# 	# print(movie.character_set.all())

	# # OR Query
	# movs = Movie.objects.filter(Q(title__startswith='Avengers') | Q(title__startswith='Thor'))
	# print(movs)

	# #AND Query
	# movs = Framework.objects.filter(Q(langauge__name='Python') & Q(name='Django'))
	# print(movs)

	# # UNION Query
	# skills = Language.objects.all().values('name').union(Framework.objects.all().values('name'))
	# print()
	# print(skills)

	# NOT (exclude) Using Q
	frameworks = Framework.objects.filter(~Q(langauge__name='Javascript')&~Q(name__startswith='Spring')).only('name')
	print(frameworks)

	context ={}
	# context={'quizzes':sportsQuizzes , 'categoryID':categoryID , 'colors':colors, 'movcar': cap}
	return render(request,'index.html',context)

