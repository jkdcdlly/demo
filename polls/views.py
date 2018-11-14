# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render

from .models import PostList, PostDetail, GameInfo


def index_view(request):
    """
    首页
    :param request:
    """
    start_with = request.GET.get('game_name')
    game_name = "" if start_with is None or start_with == "Hot" else start_with
    game_info_list = GameInfo.objects.filter(Q(game_name__startswith=game_name) &
                                             Q(post_num__gt=0)
                                             ).order_by('-post_num')
    return render(request, 'polls/index.html', {'game_info_list': game_info_list})


def search_view(request):
    """
    搜索
    :param request:
    """
    game_name = request.GET["game_name"]
    game_info_list = GameInfo.objects.filter(Q(game_img_url__contains=game_name) &
                                             Q(post_num__gt=0)
                                             ).order_by('-post_num')
    return render(request, 'polls/index.html', {'game_info_list': game_info_list})


def start_view(request, game_name):
    """
    字母搜索
    :param game_name:
    :param request:
    """
    game_name__startswith = "" if game_name is None or game_name == "Hot" else game_name
    game_info_list = GameInfo.objects.filter(Q(game_name__startswith=game_name__startswith) &
                                             Q(post_num__gt=0)
                                             ).order_by('-post_num')
    return render(request, 'polls/index.html', {'game_info_list': game_info_list})


def get_post_list(request, game_name):
    """
    列表页
    :param game_name:
    :param request:
    """
    GameInfo.objects.filter(game_name=game_name).update(post_num=PostList.objects.count())
    contact_list = PostList.objects.filter(game_name=game_name).order_by('-create_time').all()
    paginator = Paginator(contact_list, 25)  # Show 25 contacts per page

    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'polls/list.html', {'contacts': contacts, 'game_name': game_name})


def get_post_detail(request, game_name, id):
    """
    详情页
    :param id:
    :param game_name:
    :param request:
    """
    contact_list = PostList.objects.filter(game_name=game_name).order_by('-create_time')[0:10]
    postdetail = PostDetail.objects.filter(id=id).first()
    return render(request, 'polls/posts.html', {
        'contact_list': contact_list,
        'postdetail': postdetail
    })


def get_post_detail_by_id(request, id):
    """
    详情页
    :param request:
    :param id:
    """
    postdetail = PostDetail.objects.filter(id=id).first()
    contact_list = PostList.objects.filter(game_name=postdetail.game_name).order_by('-create_time')[0:10]
    return render(request, 'polls/posts.html', {
        'contact_list': contact_list,
        'postdetail': postdetail
    })


def google(request):
    return render(request, "polls/google9a8e8bb776390296.html")
