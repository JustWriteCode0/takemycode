from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Publication
from .forms import PublicationForm


def home_page(request):
    posts = Publication.objects.all()[::-1] 
    if request.method == 'POST':
        '''if user click on remove button - delete post''' 
        post = get_object_or_404(Publication, id=request.POST.get('delete_post'))
        post.delete()
        return HttpResponseRedirect(reverse('home_page'))
    return render(request, 'posts/html/main_page.html', {'posts': posts})

def add_post(request):
    ''' if user is authenticated create post else redirect to login page '''
    if request.user.is_authenticated: 
        form = PublicationForm
        if request.method == 'POST':
            form = PublicationForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('/')
        return render(request, 'posts/html/create_post.html', {'form': form})        
    return redirect('account/login')            



def like_post(request, pk):
    ''' if user like post add, if user has already liked, remove '''
    post = get_object_or_404(Publication, id=request.POST.get('post_id'))
    try: 
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
    except TypeError:
        return redirect('login')            
    return HttpResponseRedirect(reverse('home_page'))


