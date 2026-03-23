from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, ProductForm
from .models import Post, Product

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
    return render(request, "update_post.html", context)

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

def products(request):
    q = request.GET.get('q', '')
    if q:
        products = Product.objects.filter(name__icontains=q)
    else:
        products = Product.objects.all()
    context = {
        "products": products,
        "query": q,
    }
    return render(request, "products.html", context)

def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products")
    else:
        form = ProductForm()
    context = {
        "form": form
    }
    return render(request, "create_product.html", context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_detail.html", {"product": product})

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_detail", pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, "edit_product.html", {"form": form, "product": product})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect("products")
    return render(request, "delete_product.html", {"product": product})