import imp
from django.shortcuts import render
from miamibooking.models import jetski, ponton, yacht
from django.core.mail import send_mail
from django.http import HttpResponse
from pubgpot import settings
# Create your views here.


def miamibooking(request):

    if request.method=="POST":
        clientname = request.POST['clientname']
        contact =  request.POST['contact']
        quantity = request.POST['quantity']

        ins = jetski(clientname=clientname, contact= contact, quantity=quantity)
        ins.save()
    return render(request, 'servicedetail1.html')


def miamibooking2(request):

    if request.method=="POST":
        clientname = request.POST['clientname']
        contact =  request.POST['contact']
        quantity = request.POST['quantity']

        ins = jetski(clientname=clientname, contact= contact, quantity=quantity)
        ins.save()
    return render(request, 'servicedetail2.html')


def jetskibooking(request):

    if request.method=="POST":
        clientname = request.POST['clientname']
        contact =  request.POST['contact']
        quantity = request.POST['quantity']

        ins = jetski(clientname=clientname, contact= contact, quantity=quantity)
        ins.save()
    return render(request, 'servicedetail1.html')


def pontonbooking(request):

    if request.method=="POST":
        clientname = request.POST['clientname']
        contact =  request.POST['contact']
        quantity = request.POST['quantity']

        ins = ponton(clientname=clientname, contact= contact, quantity=quantity)
        ins.save()
    return render(request, 'servicedetail1.html')

def yachtbooking(request):

    if request.method=="POST":
        clientname = request.POST['clientname']
        contact =  request.POST['contact']
        quantity = request.POST['quantity']

        ins = yacht(clientname=clientname, contact= contact, quantity=quantity)
        ins.save()
    return render(request, 'servicedetail1.html')


def mailsend(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name' : name,
            'email' : email,
            'subject' : subject,
            'message' : message 

        }
        message = '''
        New message: {}

        From: {}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', ['iamnine07@gmail.com'])

def SendMail(request):
    if request.method == 'POST':
        email=request.POST['email']
        msg=request.POST['msg']
        bdate = request.POST['bookingdate']
        subject='Welcome to Sunil Code'
        message=msg
        from_email=settings.EMAIL_HOST_USER
        recipent_list=[email]
        send_mail(subject,message,bdate, from_email,recipent_list,fail_silently=True)

        return render(request, 'servicedetail1.html')
        # return HttpResponse('your message has been send successfully.')


def servicedetail2(request):
    # return render(request, 'about.html')
    return render(request, 'servicedetail2.html')

def servicedetail3(request):
    # return render(request, 'about.html')
    return render(request, 'servicedetail3.html')

def servicedetail4(request):
    # return render(request, 'about.html')
    return render(request, 'servicedetail4.html')

def servicedetail5(request):
    # return render(request, 'about.html')
    return render(request, 'servicedetail5.html')

def servicedetail6(request):
    # return render(request, 'about.html')
    return render(request, 'servicedetail6.html')