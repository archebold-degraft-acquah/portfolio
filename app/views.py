from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ContactForm, ReplyMessageForm
from django.contrib import messages
from django.http import JsonResponse


def user_portfolio(request, user_name):
    user = get_object_or_404(User, username=user_name)
    form = ContactForm()
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = user
            contact.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            messages.success(request, "Your message was sent successfully")
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False})
            messages.error(request, "Your message could not be submitted. Please check the information you provided, making sure you've filled all required fields and try submitting again")
    
    context = {"user": user, "title": f"{user.username}'s Portfolio", "form": form}
    return render(request, "app/portfolio.html", context)


@login_required
def user_messages(request, user_name):
    user = get_object_or_404(User, username=user_name)
    messages = user.contact_set.all()
    context = {"messages": messages, "title": "Messages"}
    return render(request, "app/messages.html", context)


@login_required
def reply_messages(request, user_name, message_id):
    user = get_object_or_404(User, username=user_name)
    message = user.contact_set.get(pk=message_id)
    form = ReplyMessageForm()
    context = {"form": form, "title": f"Replying to {message.name}'s message"}
    return render(request, "app/reply_message.html", context)

    if request.method == "POST":
        form = ReplyMessageForm(request.POST)
        if form.is_valid():
            reply =form.save(commit=False)
            reply.to_user.email = message.email
            reply.save()
            messages.success(request, "Reply sent successfully")
            return redirect("app:messages")
        else:
            messages.error(request, "Your message could not be sent. Please check your information and try again")
            return render(request, "app/reply_message.html", context)
