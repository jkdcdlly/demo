from django.shortcuts import render, get_object_or_404, Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question, Trade, WonList, PostList, PostDetail, GameInfo

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class IndexView(generic.ListView):
    model = GameInfo
    template_name = 'polls/index.html'
    context_object_name = 'game_info_list'

    def get_queryset(self):
        """Return the last five published questions."""
        start_with = self.request.GET.get('game_name')
        print(
            "IndexViewIndexViewIndexViewIndexView=====================================================================",
            start_with)
        return GameInfo.objects \
            .filter(game_name__startswith=("" if start_with is None or start_with == "Hot" else start_with)) \
            .order_by('game_name')


def searchView(request):
    """Return the last five published questions."""
    game_name = request.GET["game_name"]
    game_info_list = GameInfo.objects \
        .filter(game_img_url__contains=game_name) \
        .order_by('game_name')
    return render(request, 'polls/index.html', {'game_info_list': game_info_list})


def startView(request, game_name):
    """Return the last five published questions."""
    print("=====================================================================", game_name)
    game_info_list = GameInfo.objects \
        .filter(game_name__startswith=("" if game_name is None or game_name == "Hot" else game_name)) \
        .order_by('game_name')
    return render(request, 'polls/index.html', {'game_info_list': game_info_list})


class DetailView(generic.DetailView):
    model = Question
    print("===========DetailView==========")
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    print("===========ResultsView==========")
    template_name = 'polls/results.html'


class TradeView(generic.DetailView):
    model = Trade

    print("===========DetailView==========")
    template_name = 'polls/detail.html'


def WonListView(request):
    contact_list = WonList.objects.all()
    paginator = Paginator(contact_list, 10)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'polls/list.html', {'contacts': contacts})


def PostListView(request, game_name):
    print("=teste==========================================")
    contact_list = PostList.objects.filter(game_name=game_name).order_by('-create_time').all()
    paginator = Paginator(contact_list, 25)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'polls/list.html', {'contacts': contacts})


class PostDetailView(generic.DetailView):
    model = PostDetail
    print("===========PostDetailView==========")
    template_name = 'polls/posts.html'
    # return render(request, 'polls/posts.html')


def get_post_detail(request, game_name, id):
    contact_list = PostList.objects.filter(game_name=game_name).order_by('-create_time')[0:10]
    postdetail = PostDetail.objects.filter(id=id).first()
    return render(request, 'polls/posts.html', {
        'contact_list': contact_list,
        'postdetail': postdetail
    })


# class PostDetail(generic.DetailView):
#     model = PostDetail
#     print("===========PostDetailView==========")
#     template_name = 'polls/posts.html'
#     # return render(request, 'polls/posts.html')


def vote(request, question_id):
    print("===========vote==========")
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def google(request):
    return render(request, "polls/google9a8e8bb776390296.html")
