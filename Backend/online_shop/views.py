from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post

# Create your views here.
def home(request):
    text = "Discover our curated collection of products and enjoy a seamless shopping experience with fast delivery and excellent customer support."
    latest_posts = Post.objects.all().order_by('-id')[:3]
    context = {"text": text, "latest_posts": latest_posts}
    return render(request, "home.html", context)


def about(request):
    text = "About us"
    context = {"text": text}
    return render(request, "about.html", context)


def posts(request):
    q = request.GET.get('q', '')
    if q:
        posts = Post.objects.filter(title__icontains=q)
    else:
        posts = Post.objects.all()
    context = {
        "posts": posts,
        "query": q,
    }
    return render(request, "posts.html", context)


def create_posts(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts")
    else:
        form = PostForm()
    context = {
        "form": form
    }
    return render(request, "create_posts.html", context)

def update_posts(request, pk: int):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("posts")
    else:
        form = PostForm(instance=post)
    context = {
        "form": form
    }
    return render(request, "update_posts.html", context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post_detail.html", {"post": post})


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "edit_post.html", {"form": form, "post": post})


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("posts")
    return render(request, "delete_post.html", {"post": post})
