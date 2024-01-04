from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from blog.models import Post


def post_list(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 2)
    page_number = request.GET.get('page',1)
    try:
        posts = paginator.page(page_number) 
    except EmptyPage:
       posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
    return render(request, "blog/post/list.html", {"posts":posts})


def post_detail(request, post):
    try:
        post2 = Post.objects.get(slug=post)
    except Post.DoesNotExist:
        raise Http404("! Post Not Found !")
    return render(request, "blog/post/detail.html", {"post":post2})