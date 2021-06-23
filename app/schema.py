from graphene_django import DjangoObjectType, DjangoListField
from .models import Category, Quizzes, Question, Answer
import graphene

# class BooksType(DjangoObjectType):
# 	class Meta:
# 		model = Books
# 		fields = ("id","title","excerpt")

# class Query(graphene.ObjectType):
# 	all_books = graphene.List(BooksType)

# 	def resolve_all_books(root,info):
# 		return Books.objects.all()

# schema = graphene.Schema(query=Query)

class CategoryType(DjangoObjectType):
	class Meta:
		model = Category
		fields = ("id","name")

class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id","title","category","quiz")

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title","quiz")

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question","answer_text")

class Query(graphene.ObjectType):
	quiz = DjangoListField(QuizzesType)
	
	# def resolve_quiz(root, info):
	# 	return f"String"

schema =  graphene.Schema(query=Query)