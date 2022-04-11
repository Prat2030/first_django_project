from django.shortcuts import render,HttpResponse
from datetime import datetime

from home.models import Contact

# Create your views here.

def index(request):
    context = {
        "variable":"value"
    }
    return render(request,'index.html',context)
    # return HttpResponse('This is HomePage')

#  Here we come from the urls.py file and we get the request and we get the path.
#  from here we return the value either in terms of template which gets 
#  rendered or just a String in the form of HttpResponse.
def about(request):
    # return HttpResponse('This is about Page')
    return render(request,'about.html')

def services(request):
    # return HttpResponse('This is services Page')
    return render(request,'services.html')
    
def contact(request):
    
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()

    return render(request,'contact.html')