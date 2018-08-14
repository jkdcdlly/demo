from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search', views.searchView, name='search'),
    path('start/<str:game_name>', views.startView, name='start'),
    path('accounts/<str:game_name>/', views.PostListView, name='list'),
    # path('accounts/<str:game_name>/<str:pk>/', views.PostDetailView.as_view(), name='details'),
    path('accounts/<str:game_name>/<str:id>/', views.get_post_detail, name='details'),
    path('<str:game_name>/', views.PostListView, name='lists'),
    path('<str:game_name>/<str:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('mmo-trading-market/<str:pk>/', views.PostDetailView.as_view()),
    # path('<str:pk>/', views.TradeView.as_view(), name='detail'),
    # path('<str:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<str:question_id>/vote/', views.vote, name='vote'),
]
