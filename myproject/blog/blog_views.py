# myapp/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'myapp/blog_list.html', {'blogs': blogs})

def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'myapp/blog_detail.html', {'blog': blog})

def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'myapp/blog_form.html', {'form': form})

def blog_update(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'myapp/blog_form.html', {'form': form})

def blog_delete(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, 'myapp/blog_confirm_delete.html', {'blog': blog})
