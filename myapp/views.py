from django.shortcuts import render
from .models import user
from .forms import Studentregi

# Create your views here.
def studentdata(request):
    if request.method=="post":
        fm=Studentregi(request.post)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            alldata=user(name=nm,email=em,password=pw)
            alldata.save()
    else:
        fm=Studentregi()
        data=user.objects.all()
    return render(request,'main/addstudent.html',{'form':fm,'data':data})

