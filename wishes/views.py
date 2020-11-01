from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, Group
from .models import Wish, Gallery, Reply
from .forms import WishForm, ReplyForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    wishes = Wish.objects.all()
    context = {
        'wishes': wishes,
    }
    return render(request, 'index.html', context)

def new(request):
    form = WishForm()
    if request.method == 'POST':
        form = WishForm(request.POST)
        if form.is_valid():
            wish = Wish(
                author = form.cleaned_data['author'],
                email = form.cleaned_data['email'],
                desc = form.cleaned_data['description'],
                body = form.cleaned_data['body'],
            )
            wish.save()
            author = form.cleaned_data['author']
            message = form.cleaned_data['body']
            email = form.cleaned_data['email']
            context = {
                'author': author,
                'message': message,
            }
            subject = 'THANK YOU FOR THE BIRTHDAY WISH'
            message = f'Hi {author}, thank you for sending Ayomikun a birthday wish. Your ' \
                      f'wish has been recorded and would be published upon vetting.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, 'elso4real@yahoo.com']
            send_mail(subject, message, email_from, recipient_list)

            return render(request, 'success.html', context)
    context = {
        'form':form,
    }
    return render(request, 'new.html', context)

def wish_list(request):
    wishes = Wish.objects.filter(status='ok').order_by('-created_on')
    context = {
        'wishes': wishes,
    }
    return render(request, 'wish_list.html', context)

def waiting(request):
    wishes = Wish.objects.filter(status='Not Published').order_by('-created_on')
    context = {
        'wishes': wishes,
    }
    return render(request, 'wish_list.html', context)

@login_required
def wish_detail(request,pk):
    wish = Wish.objects.get(pk=pk)
    form = ReplyForm()
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = Reply(
                msg=form.cleaned_data['msg'],
                wish=wish,
            )
            msg = str(form.cleaned_data['msg'])
            print(msg)
            subject = f'THANK YOU {wish.author}'
            message = f'{msg}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [wish.email, 'elso4real@yahoo.com']
            send_mail(subject, message, email_from, recipient_list)
            reply.save()
    replies = Reply.objects.filter(wish=wish)
    context = {
        'replies': replies,
        'form': form,
        'wish': wish,
    }
    return render(request, 'wish_detail.html', context)

@login_required
def reply(request,pk):
    wish = Wish.objects.get(pk=pk)
    form = WishForm()
    context = {
        'wish': wish,
        'form': form,
    }
    if request.method == 'POST':
        form = WishForm(request.POST)
        msg = form.cleaned_data['reply']
        context = {
            'wish': wish,
            'form': form,
        }
        subject = 'THANK YOU FOR THE BIRTHDAY WISH'
        message = wish.reply
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [wish.email, 'elso4real@yahoo.com']
        send_mail(subject, message, email_from, recipient_list)

    return render(request, 'reply.html', context)

def gallery(request):
    images = Gallery.objects.all()
    context = {
        'images': images,
    }
    return render(request, 'gallery.html', context)
