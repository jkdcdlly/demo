from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search', views.searchView, name='search'),
    path('start/<str:game_name>', views.startView, name='start'),
    path('accounts/<str:game_name>/', views.PostListView, name='list'),
    path('accounts/<str:game_name>/<str:id>/', views.get_post_detail, name='details'),
    path('accounts/<str:game_name>/<str:id>/site_index', views.get_post_detail, name='details'),

    path('<str:game_name>/', views.PostListView, name='lists'),
    # path('<str:game_name>/<str:id>/', views.get_post_detail_byid, name='detail'),
    path('mmo-trading-market/<str:id>/', views.get_post_detail_byid),
]
