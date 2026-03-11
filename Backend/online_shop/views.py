from django.shortcuts import render

# Create your views here.
def home(request):
    text = "Hello world"
    content = {"text": text}
    return render(request, "home.html", content)


def about(request):
    text = "About us"
    content = {"text": text}
    return render(request, "about.html", content)
