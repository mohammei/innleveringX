from django.shortcuts import render

def frontpage(request):
    return render(request, 'theme/frontpage.html')
# Create your views here.
