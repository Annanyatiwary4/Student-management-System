from django.shortcuts import render

# Create your views here.
def studentHomepage(request):
    return render(request,'studentapp/studentHomepage.html')
