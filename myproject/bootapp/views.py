from django.shortcuts import render

# Create your views here.
def boot(request):
    return render(request, 'boot.html')

def about(request):
    return render(request, 'about.html')