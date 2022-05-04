from django.shortcuts import redirect, render, get_object_or_404
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


def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    try:
        dulieu = request.POST["choice"]
        c = q.choice_set.get(pk=dulieu)
    except:
        HttpResponse("lỗi khẳng có choice")
    c.vote = c.vote + 1
    c.save()
    return render(request, "polls/result.html", {"q": q})


def tailieu(request):
    return redirect('https://docs.google.com/document/d/1QG9lc-cs0MRLVJ-lwQgkT-kSIJGnqJ2q/edit?usp=sharing&ouid=108391021487747039184&rtpof=true&sd=true')


def cv(request):
    return redirect('https://drive.google.com/file/d/1JXFw1GIIGq3BtR2_KI2RWqxLQ5cuOcLr/view?usp=sharing')


def xstk(request):
    return redirect('https://drive.google.com/file/d/1erLldB6yXAKDwir3hTVpJuvlGvBCAjNF/view?usp=sharing')


def xstk1(request):
    return redirect('https://drive.google.com/file/d/1m972bRvQjhU4nRB2kqVM9WWHrWJh0BWd/view?usp=sharing')
