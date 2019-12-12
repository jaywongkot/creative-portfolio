from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.

def post_list(request):
  posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') # add to published_date to display newest post first. 
  return render(request, '../templates/post_list.html', { 'blogs': posts }) # string in '' use to loop through post in post_list.html

def post_detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  return render(request, '../templates/post_detail.html', {'post': post}) # string in '' use to check condition in post_detail.html

def post_new(request):
  form = PostForm()
  return render(request, '../templates/post_edit.html', {'form': form}) # string in '' use to display form in post_edit.html
