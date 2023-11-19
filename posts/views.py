from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from .services import ModelService as service  # ---------------- v1 DANE Z MODELU -------------------------
# from .services import FakerPostService as service # ------------v2 DANE Z FAKERA -------------------------


# Create your views here.


def list(request):
    posts_list = service.list()
    return render(request, 'posts/list.html', {"posts_list": posts_list})


def add(request):
    if request.method == "POST":
        ob = service.create(request.POST)
        ob.save()
        return redirect('posts_list')
    else:
        ob = PostForm()
        return render(request, 'posts/add.html', {"form": ob})


def details(request, id):
    ob = service.get(id)
    return render(request, 'posts/details.html', {"details": ob})



