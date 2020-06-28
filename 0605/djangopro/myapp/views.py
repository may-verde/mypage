from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import BlogPost

def main(request):
    blogs = BlogPost.objects
    return render(request, 'home.html', {'blogpost':blogs})

def detail(request, post_id):
    details = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'detail.html', {'detail':details})

def write(request):
    return render(request, 'write.html')

def create(request):
    blog = BlogPost()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))