from django.shortcuts import render , HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse("this is home page")
    context={
        'variable': "groot"
    }
    return render(request,'index.html',context)

def about(request):
    return HttpResponse("this is home about page")

def services(request):
    return HttpResponse("this is service page")

def contact(request):
    return HttpResponse("this is home about page")