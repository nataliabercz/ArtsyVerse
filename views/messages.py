from django.contrib.auth import models as auth_models
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from main import models, forms

HTML_TEMPLATE = 'main/user_page/messages.html'


@login_required
def get_messages(request, recipient_id=None):
    get_conversations(request)
    try:
        last_recipient = auth_models.User.objects.get(id=recipient_id)
    except:
        last_recipient = None
    grouped_messages = {}
    sent_messages = models.UserProfile.objects.get(user_id=request.user.id).messages.all()
    for message in models.Message.objects.all().order_by('-id'):
        recipient = message.recipient
        sender = models.UserProfile.objects.get(messages=message).user
        for msg in sent_messages:
            if message.id == msg.id:
                grouped_messages.setdefault(recipient, {})
                grouped_messages[recipient].setdefault('messages', []).append(message)
                if not last_recipient:
                    last_recipient = recipient
        if str(recipient) == str(request.user):
            grouped_messages.setdefault(sender, {})
            grouped_messages[sender].setdefault('messages', []).append(message)
            if recipient_id == sender.id:
                models.Message.objects.filter(id=message.id).update(is_read=True)
            if not message.is_read:
                grouped_messages[sender]['unread'] = grouped_messages[sender].get('unread', 0) + 1
            if not last_recipient:
                last_recipient = sender
    for profile in models.UserProfile.objects.all():
        grouped_messages.setdefault(profile.user, {})
    return render(request, HTML_TEMPLATE,
                  {'grouped_messages': grouped_messages, 'current_recipient': last_recipient,
                   'form_message_send': forms.MessageSendForm(initial={'recipient': last_recipient})})


def search_users(request):
    return render(request, HTML_TEMPLATE)


class UserAutocomplete(View):
    @staticmethod
    def get(request):
        query = request.GET.get('term', '')
        users = auth_models.User.objects.filter(username__icontains=query)[:10]
        results = [f'{usr.first_name} {usr.last_name}' for usr in users]
        return JsonResponse(results, safe=False)


def search_recipients(request):
    name = request.GET['search_query'].split(' ')
    return redirect(f'/user/messages/{auth_models.User.objects.get(first_name=name[0], last_name=name[1]).id}')


def get_conversations(request):
    # get all users that messages were sent/received
    pass


def get_conversation(request):
    # get messages from users from get_conversations
    pass


def send_message(request):
    # add message to UserProfile
    if request.method == 'POST':
        form_message_send = forms.MessageSendForm(request.POST)
        if form_message_send.is_valid():
            message = form_message_send.save()
            models.UserProfile.objects.get(user=request.user).messages.add(message)
    return redirect(request.META['HTTP_REFERER'])
