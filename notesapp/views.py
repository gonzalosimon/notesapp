from django.shortcuts import render

def about(request):
    return render(request, 'notes/about.html')
