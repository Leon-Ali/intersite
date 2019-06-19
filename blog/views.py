from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Message

def index(request):
    messages = Message.objects.all()
    return render(request, 'blog/index.html',
           {'messages':messages})


def send_message(request):
    message = Message(content = request.POST['content'])
    message.save()
    return HttpResponseRedirect('/index/')