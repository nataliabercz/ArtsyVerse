from django.shortcuts import render, redirect
from main import models, forms

HTML_TEMPLATE = 'main/user_page/messages.html'


def get_messages(request):
    get_conversations(request)
    return render(request, HTML_TEMPLATE, {'messages': models.Message.objects.all().order_by('id')})


def search_users(request):
    # all userprofiles
    pass


def get_conversations(request):
    # get all users that messages were sent/received
    pass


def get_conversation(request):
    # get messages from users from get_conversations
    pass


def send_message(request):
    pass
