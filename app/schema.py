from graphene_django import DjangoObjectType, DjangoListField
from .models import Category, Quizzes, Question, Answer
import graphene


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

	questions = graphene.Field(QuestionType, id=graphene.Int())
	answers = graphene.List(AnswerType, id=graphene.Int())
	categories = graphene.List(CategoryType, id=graphene.Int())

	def resolve_questions(root, info, id):
		return Question.objects.get(pk=id)
	def resolve_answers(root, info, id):
		return Answer.objects.filter(question=id)
	def resolve_categories(root, info):
		return Category.objects.all()


class CategoryMutation(graphene.Mutation):
	class Arguments:
		id = graphene.ID()
		name = graphene.String(required=True)

	category = graphene.Field(CategoryType)	

	@classmethod
	def mutate(cls, root, info, name): # Add id when needed
		category = Category(name=name)
		category.name = name
		category.save()
		# # For delete:-
		# category.delete()
		# # No need to pass name as attribute
		return CategoryMutation(category=category)


class Mutation(graphene.ObjectType):
	update_category = CategoryMutation.Field()
	


schema =  graphene.Schema(query=Query, mutation=Mutation)


# Queries:-
# query getQuestionAnswers($id : Int = 2){
#   questions(id:$id)
#   {
#     title
#   }
#   answers(id:$id)
#   {
#     answerText
#   }
# }

# mutation addCategory
# {
#   updateCategory(name : "Game of Thrones")
#   {
#     category{
#       name
#     }
#   }
  
# }