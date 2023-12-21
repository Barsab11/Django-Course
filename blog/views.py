from django.shortcuts import render,get_object_or_404
from django.http import Http404
from blog.models import Post


def post_list(request):
    post = Post.objects.all()
    return render(request, "blog/post/list.html", {"post1":post})


def post_detail(request, id):
    try:
        post2 = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404("! Post Not Found !")
    return render(request, "blog/post/detail.html", {"post":post2})