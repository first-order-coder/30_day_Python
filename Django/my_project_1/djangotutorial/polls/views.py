from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import get_object_or_404, render
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone


# we are replacing the function based views with generic views(class based views)

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     # template = loader.get_template("polls/index.html")
#     # return HttpResponse(template.render(context, request))
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/index.html", context) #instead of the above commented two lines we can use this render shortcut

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """ Retrun the Last five published questions (not including those set to be published in the future). """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question Doesn't exist")
    
#     question = get_object_or_404(Question, pk=question_id) #takes the Django model as its first argument and an arbitrary number of keyword arguments raises 404 error if the object doesnt exist
#     context = {"question": question}
#     return render(request, "polls/detail.html", context)

class DetailView(generic.DetailView):
    def get_queryset(self) -> QuerySet[Any]:
        return Question.objects.filter(pub_date__lte=timezone.now())
    
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = {"question": question}
#     return render(request, "polls/results.html", context)

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request, 
            "polls/detail.html",
            {
                "question":question,
                "error_message":"You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id, )))
        

