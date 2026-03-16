from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostsForm
from .models import Posts

# Create your views here.
def home(request):
    text = "Discover our curated collection of products and enjoy a seamless shopping experience with fast delivery and excellent customer support."
    latest_posts = Posts.objects.all().order_by('-id')[:3]
    context = {"text": text, "latest_posts": latest_posts}
    return render(request, "home.html", context)


def about(request):
    text = "About us"
    context = {"text": text}
    return render(request, "about.html", context)


def posts(request):
    q = request.GET.get('q', '')
    if q:
        posts = Posts.objects.filter(title__icontains=q)
    else:
        posts = Posts.objects.all()
    context = {
        "posts": posts,
        "query": q,
    }
    return render(request, "posts.html", context)


def create_posts(request):
    context = {
        "form": PostsForm()
    }
    if request.method == "POST":
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("posts")   
    return render(request, "create_posts.html", context)


def post_detail(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    return render(request, "post_detail.html", {"post": post})


def edit_post(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    if request.method == "POST":
        form = PostsForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostsForm(instance=post)
    return render(request, "edit_post.html", {"form": form, "post": post})


def delete_post(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("posts")
    return render(request, "delete_post.html", {"post": post})
