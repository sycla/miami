from django.shortcuts import render
from matchregis.models import matchregistration, duomatchregistration, squadmatchregistration
# Create your views here.

def matchregis(request):

    if request.method=="POST":
        characterid = request.POST['characterid']
        transid =  request.POST['transactionid']
        phone = request.POST['phone']

        ins = matchregistration(characterid=characterid, transid= transid, phone=phone)
        ins.save()
    return render(request, 'matchregis.html')

def duomatchregis(request):

    if request.method=="POST":      
        duocharacterid1 = request.POST['duocharacterid1']
        duocharacterid2 = request.POST['duocharacterid2']
        duotransactionid =  request.POST['duotransactionid']
        duophone = request.POST['duophone']

        ins = duomatchregistration(duocharacterid1=duocharacterid1,duocharacterid2=duocharacterid2, duotransactionid= duotransactionid, duophone=duophone)
        ins.save()
    return render(request, 'duomatchregis.html')

def squadmatchregis(request):

    if request.method=="POST":      
        squadcharacterid1 = request.POST['squadcharacterid1']
        squadcharacterid2 = request.POST['squadcharacterid2']
        squadcharacterid3 = request.POST['squadcharacterid3']
        squadcharacterid4 = request.POST['squadcharacterid4']
        squadtransactionid =  request.POST['squadtransactionid']
        squadphone = request.POST['squadphone']

        ins = squadmatchregistration(squadcharacterid1=squadcharacterid1,squadcharacterid2=squadcharacterid2,squadcharacterid3=squadcharacterid3,squadcharacterid4=squadcharacterid4, squadtransactionid= squadtransactionid, squadphone=squadphone)
        ins.save()
    return render(request, 'squadmatchregis.html')