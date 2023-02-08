from django.shortcuts import render
from django.http import HttpResponse
from .models import Registration
from .models import Winnings
from .models import matchschedule
from .models import sliderimg
# Create your views here.

def home(request):

    r1 = Registration.objects.all()
    w1 = Winnings.objects.all()
    s2 = sliderimg.objects.all()
    mm = matchschedule.objects.all()

    # return render(request, 'home.html', {'r1': r1, 'w1':w1, 's2':s2, 'mm': mm})
    return render(request, 'miamihome.html')


def profile(request):

    r1 = Registration.objects.all()
    return render(request, 'profile.html', {'r1': r1})

def about(request):
    # return render(request, 'about.html')
    return render(request, 'miamiabout.html')

def miamiabout(request):
    # return render(request, 'about.html')
    return render(request, 'miamiabout.html')

def miamiservices(request):
    # return render(request, 'about.html')
    return render(request, 'miamiservices.html')

def miamiboats(request):
    # return render(request, 'about.html')
    return render(request, 'miamiboats.html')

def miamicontact(request):
    # return render(request, 'about.html')
    return render(request, 'miamicontact.html')


def servicedetail1(request):
    # return render(request, 'about.html')
    return render(request, 'servicedetail1.html')


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