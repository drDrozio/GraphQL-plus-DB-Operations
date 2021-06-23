from django.urls import path, include
from graphene_django.views import GraphQLView
from .schema import schema
from . import views

urlpatterns = [
    path('graphql',GraphQLView.as_view(graphiql=True, schema=schema)),
    path('databasequeries',views.databaseQueries,name='databasequeries')
]
 