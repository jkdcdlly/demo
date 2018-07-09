from django.urls import path

from . import views

# registered namespace
# app_name = 'polls'
# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
#
# ]

app_name = 'polls'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    # path('<str:pk>/', views.TradeView.as_view(), name='detail'),
    path('', views.PostListView, name='list'),
    path('mmo-/trading-market/<str:pk>/', views.PostDetailView.as_view(), name='details'),
    # path('<str:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<str:question_id>/vote/', views.vote, name='vote'),

]
