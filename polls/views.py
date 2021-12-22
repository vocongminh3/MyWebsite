from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    myName = 'Minh'
    taisan = ["Phone", 'Computer', "Phane"]
    conText = {"name": myName, "taisan": taisan}
    return render(request, "polls/index.html", conText)
