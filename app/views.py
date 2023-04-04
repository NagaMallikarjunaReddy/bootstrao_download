from django.shortcuts import render

# Create your views here.
def bsd(request):
    return render(request,'bootdownload.html')