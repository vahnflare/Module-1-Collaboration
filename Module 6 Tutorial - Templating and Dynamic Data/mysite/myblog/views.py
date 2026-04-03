from django.shortcuts import render

def home(request):
    posts = [
        {"title": "First Post", "text": "This is my first Django post"},
        {"title": "Second Post", "text": "Learning Django is fun"},
    ]
    
    return render(request, 'home.html', {'posts': posts})