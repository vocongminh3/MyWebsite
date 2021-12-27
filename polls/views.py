from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
# Create your views here.


def index(request):
    myName = 'Minh'
    taisan = ["Phone", 'Computer', "Phane"]
    conText = {"name": myName, "taisan": taisan}
    return render(request, "polls/index.html", conText)


def viewlist(request):
    # get_object_or_404 have error if data is none
    # get_object_or_404 have 2 attribute model  and condition dieu kien example Question , qusetion_text = "Do you have a girlfriend"
    list_question = Question.objects.all()
    context = {"dsquest": list_question}
    return render(request, "polls/question.html", context)


def detailView(request, question_id):
    q = Question.objects.get(pk=question_id)
    return render(request, "polls/detailQuestion.html", {"qs": q})

def vote(request,question_id):
    q = Question.objects.get(pk=question_id)
    data = request.POST["choice"]
    return HttpResponse(data)
