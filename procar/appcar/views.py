from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.conf import settings

# Create your views here.

def registerpage(request):
    if(request.method=='POST'):
        username=request.POST.get('username')
        useremail=request.POST.get('useremail')
        userphone=request.POST.get('userphone')
        userimg=request.FILES.get('userimg')
        userpass=request.POST.get('userpass')
        usercpass=request.POST.get('usercpass')
        if(userpass==usercpass):
            data=userregisterpage(username=username,useremail=useremail,userphone=userphone,userimg=userimg,userpass=userpass)
            data.save()
            return redirect(loginpage)
        else:
            return HttpResponse('failed')
    return render(request,'register.html')

def loginpage(request):
    if(request.method=='POST'):
        useremail=request.POST.get('useremail')
        userpass=request.POST.get('userpass')
        data=userregisterpage.objects.all()
        for i in data:
            if(i.useremail==useremail and i.userpass==userpass):
                request.session['userid']=i.id
                return redirect(firstpage)
        else:
            return HttpResponse('not correct')
    return render(request,'login.html')
def firstpage(request):
    id1=request.session['userid']
    db=userregisterpage.objects.get(id=id1)
    return render(request,"index.html",{'db':db})

def carregister(request):
    if(request.method=='POST'):
        carname=request.POST.get('carname')
        carimg=request.FILES.get('carimg')
        cardesc=request.POST.get('cardesc')
        carprice=request.POST.get('carprice')
        carcate=request.POST.get('carcate')
        caryear=request.POST.get('caryear')
        carmonth=request.POST.get('carmonth')
        carmodel=request.POST.get('carmodel')
        carcolor=request.POST.get('carcolor')
        carfuel=request.POST.get('carfuel')
        carversion=request.POST.get('carversion')
        caralter=request.POST.get('caralter')
        carowner=request.POST.get('carowner')
        carkilo=request.POST.get('carkilo')
        data=carregistrationpage(carimg=carimg,carname=carname,cardesc=cardesc,carprice=carprice,carcate=carcate,carcolor=carcolor,caralter=caralter,caryear=caryear,carmonth=carmonth,carmodel=carmodel,carfuel=carfuel,carversion=carversion,carowner=carowner,carkilo=carkilo)
        data.save()
        return HttpResponse('success')
    return render(request,'uploadcar.html')

def detailspage(request,id):
    data=carregistrationpage.objects.get(id=id)
    return render(request,"details.html",{'data':data})    



def sportscar(request):
    car=carregistrationpage.objects.filter(carcate__iexact='Sports')
    return render(request,'sports.html',{'car':car})    

def coupecar(request):
    car=carregistrationpage.objects.filter(carcate__iexact='Coupe')
    return render(request,'coupe.html' ,{'car':car})    

def sedancar(request):
    car=carregistrationpage.objects.filter(carcate__iexact='Sedan')
    return render(request,'sedan.html',{'car':car})  
  
def wagoncar(request):
    car=carregistrationpage.objects.filter(carcate__iexact='Wagon')
    return render(request,'wagon.html',{'car':car})    

def xuvcar(request):
    car=carregistrationpage.objects.filter(carcate__iexact='Xuv')
    return render(request,'xuv.html',{'car':car})    

def addwish(request,itemid):
    item=carregistrationpage.objects.get(id=itemid)
    db=wishitemcar(userid=request.session['userid'],item=item)
    db.save()
    return HttpResponse('added')
def wishdisplay(request):
    userid=request.session['userid']
    data=userregisterpage.objects.get(id=userid)
    db=wishitemcar.objects.filter(userid=userid)
    return render(request,"wishdisplays.html",{'data':data,'db':db})

def wishdelete(request,cartid):
    data=wishitemcar.objects.get(id=cartid) 
    data.delete()
    return redirect(wishdisplay)   