from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
def qa(request):
    return render (request, 'q&a.html')
def news(request):
    return render(request, 'news.html')
def explore(request):
    return  render(request, 'explore.html')
