from django.shortcuts import render,HttpResponse

# Create your views here.
def homepage(request):
    #logic part
    return render(request,'home/home.html')

def contents(request):
    #logic part
    return render(request,'home/contents.html')