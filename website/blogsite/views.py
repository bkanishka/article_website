from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView,  DeleteView
from django.contrib.auth.decorators import login_required
from collections import UserDict


from .forms import  URLForm
from urllib.parse import urljoin
from django.shortcuts import render, redirect


from .models import Post
from .forms import PostForm

# def home(request):
#     return render(request, 'home.html', {})
class HomeView(ListView):
    model = Post
    template_name ='home.html'
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article.html'
class AddPostView(CreateView):
    model = Post
    fields =[ 'title' ,'author', 'body']
    template_name = 'addpost.html'
class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update.html'
    fields = ['title', 'body']
@login_required
def my_articles(request):
    articles = Post.objects.filter(author=request.user)
    return render(request, 'posts.html', {'articles': articles})
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('post')

def submit_url(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            user_url = Post(author=request.user, url=url)
            user_url.save()
            return redirect('url_list')
    else:
        form = URLForm()
    return render(request, 'submit_url.html', {'form': form})

def url_list(request):
    urls =   Post.objects.filter(author=request.user)
    return render(request, 'url_list.html', {'urls': urls})


