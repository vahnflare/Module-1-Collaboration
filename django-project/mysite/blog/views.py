from django.shortcuts import render
from .forms import CommentForm
from .models import Comment

def home(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                name=form.cleaned_data['name'],
                comment=form.cleaned_data['comment']
            )
    else:
        form = CommentForm()

    comments = Comment.objects.all()

    return render(request, 'blog/home.html', {
        'form': form,
        'comments': comments
    })