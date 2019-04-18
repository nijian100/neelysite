from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello,world.You're at the polls index.")

def detail(request,question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request,qquestion_id):
    response = "You're looking ay the result %s."
    return HttpResponse(response % qquestion_id)

def vote(request,question_id):
    return HttpResponse("You're voting on question %s." % question_id)