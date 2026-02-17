from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader
from django.shortcuts import get_object_or_404, render

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")
    # return HttpResponse(template.render(context, request))
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context) #instead of the above commented two lines we can use this render shortcut

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question Doesn't exist")
    question = get_object_or_404(Question, pk=question_id) #takes the Django model as its first argument and an arbitrary number of keyword arguments raises 404 error if the object doesnt exist
    context = {"question": question}
    return render(request, "polls/detail.html", context)

def results(request, questiond_id):
    response = "You are looking at the results of the question %s."
    return HttpResponse(response % questiond_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)

