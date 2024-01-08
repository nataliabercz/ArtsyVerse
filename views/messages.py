from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from main import models, forms

HTML_TEMPLATE = 'main/user_page/messages.html'


@login_required
def get_messages(request, recipient_id=None):
    get_conversations(request)
    last_recipient = recipient_id
    grouped_messages = {}
    for message in models.Message.objects.all().order_by('-id'):
        sender = message.sender
        recipient = message.recipient
        if str(sender) == str(request.user):
            grouped_messages.setdefault(recipient.user.id, {})
            grouped_messages[recipient.user.id].setdefault('messages', []).insert(0, message)
            grouped_messages[recipient.user.id]['user'] = recipient.user
            if not last_recipient:
                last_recipient = recipient.user.id
        elif str(recipient) == str(request.user):
            grouped_messages.setdefault(sender.id, {})
            grouped_messages[sender.id].setdefault('messages', []).insert(0, message)
            grouped_messages[sender.id]['user'] = sender
            print(message.is_read)
            if recipient_id == sender.id:
                models.Message.objects.filter(id=message.id).update(is_read=True)
            print(message.is_read)
            if not message.is_read:
                grouped_messages[sender.id]['unread'] = grouped_messages[sender.id].get('unread', 0) + 1
            if not last_recipient:
                last_recipient = sender.id
    return render(request, HTML_TEMPLATE,
                  {'grouped_messages': grouped_messages, 'last_recipient': last_recipient,
                   'form_message_send': forms.MessageSendForm(
                       initial={'sender': request.user,
                                'recipient': models.UserProfile.objects.get(user_id=last_recipient)})})


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
    if request.method == 'POST':
        form_message_send = forms.MessageSendForm(request.POST)
        if form_message_send.is_valid():
            form_message_send.save()
    return redirect(request.META['HTTP_REFERER'])
