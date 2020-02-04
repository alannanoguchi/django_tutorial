from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views import View # import the parent class
from django.template import loader
from .models import Question


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


class ShowTimeView(View):   # create a view class

    # change the function-based view to be called get and add the self param

    def get(self, request):
        now = datetime.now()
        html = "<html><body>It is now {}</body></html>".format(now)
        return HttpResponse(html)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)