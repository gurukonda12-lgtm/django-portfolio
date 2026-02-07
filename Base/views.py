from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from Base import models
from Base.models import Contact

# Create your views here.
# def home(request):
#     return render(request,'home.html')

def contact(request):
    if request.method=="POST":
        print('post')
        name=request.POST.get('name')
        email=request.POST.get('email')
        content=request.POST.get('content')
        number=request.POST.get('number')
        print(name,email,content,number)

        if len(name)>1 and len(name)<30:
            pass
        else:
            messages.error(request,'Length of name should be greater than 2 and lessthan 30 words')
            return render(request,'home.html')
        
        if len(email)>1 and len(email)<30:
            pass
        else:
            messages.error(request,'invalid email try again')
            return render(request,'home.html')
        
        if len(number)>1 and len(number)<30:
            pass
        else:
            messages.error(request,'invalid number try again')
            return render(request,'home.html')
        ins=models.Contact(name=name,email=email,content=content,number=number)
        ins.save()
        messages.success(request,'Thank you for connecting me || Your message have been Saved')
        print('date has been saved to database')
        print('The reqeust is no pass')
    return render(request,'home.html')

        
        