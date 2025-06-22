from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentReg
from .models import User

# Create your views here.

def add_show(request):
    if request.method=="POST":
        fm=StudentReg(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            reg=User(name=name,email=email,password=password)
            reg.save()
            fm=StudentReg()

            
    else:
        fm=StudentReg()
    stud=User.objects.all()
    print(stud)
    for i in stud:
        print(i.name)
    return render(request,'index.html',{'form':fm,'stud':stud})

def update_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudentReg(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            msg={'msg':True}
            fm=StudentReg()

    else:
        msg={'msg':False}
        pi=User.objects.get(pk=id)
        fm=StudentReg(instance=pi)
    return render(request,'update.html',{'form':fm,'msg':msg})

def dalete_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()

    return HttpResponseRedirect('/')
