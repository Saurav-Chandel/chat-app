from django.shortcuts import render

# Create your views here.

def home(request,*args,**kwargs):
    context={}
    context['name']='saurav'
    return render(request,"chatapp/home.html",context)


