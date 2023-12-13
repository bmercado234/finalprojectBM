from django.urls import path

from . import views

# app namespace
app_name = "polls"

urlpatterns = [
    # root
    path("", views.index, name="index"),
    # question id used to link details
    path("<int:question_id>/", views.detail, name="detail"),
    # question id used to link to results of question
    path("<int:question_id>/results/", views.results, name="results"),
    # question id used to link to vote view
    path("<int:question_id>/vote/", views.vote, name="vote"),
    # create question view
    path('create_question/', views.create_question, name='create_question'),
]