from django.shortcuts import render,HttpResponse

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
    return HttpResponse('This is about Page')

def services(request):
    return HttpResponse('This is services Page')
    
def contact(request):
    return HttpResponse('This is contact Page')