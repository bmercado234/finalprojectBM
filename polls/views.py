from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from .models import Choice, Question


def index(request):
    # display latest five questions
   latest_question_list = Question.objects.order_by("-pub_date")[:5]
   return render(request, "index.html", {"latest_question_list": latest_question_list})


def detail(request, question_id):
    # question doesn't exist case
   question = get_object_or_404(Question, id=question_id)
   context = {"question": question}
    # render detail page
   return render(request, "detail.html",context)

def results(request, question_id):
    # question doesnt exist case
   question = get_object_or_404(Question, id=question_id)
   context = {"question": question}
    # render results page
   return render(request, "results.html", context)


def create_question(request):
    # get choices and question to create new question with choice and redirects to detail page on POST request
    if request.method == 'POST':
        question_text = request.POST['question_text']
        choices = request.POST.getlist('choice')
        question = Question(question_text=question_text, pub_date=timezone.now())
        question.save()
        for choice in choices:
            print(choices)
            Choice(question=question, choice_text=choice, votes=0).save()
        return HttpResponseRedirect(reverse("polls:detail", args=(question.id,)))
    else:
        # render create question page on GET request
        return render(request, 'create_question.html')


def vote(request, question_id):
    # attempt retrieving selected choice
    question = get_object_or_404(Question, id=question_id)
    try:
        selected_choice = question.choice_set.get(id=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        context = {
                "question": question,
                "error_message": "You didn't select a choice.",
            }
        return render(request,"detail.html",context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))