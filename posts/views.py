from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
# from .services import ModelService as service  # ---------------- v1 DANE Z MODELU -------------------------


from .services import FakerPostService as service # ------------v2 DANE Z FAKERA -------------------------


def app_list(request):
    return render(
        request=request,
        template_name='posts/list.html',
        context={"posts_list": service.list()}
    )


def add(request):
    if request.method == "POST":
        ob = service.create(request.POST)
        ob.save()
        return redirect('posts_list')
    return render(
        request=request,
        template_name='posts/add.html',
        context={"form": PostForm()}
    )


def details(request, id):
    return render(
        request=request,
        template_name='posts/details.html',
        context={"details": service.get(id)}
    )
