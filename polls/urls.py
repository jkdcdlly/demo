from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('search', views.search_view, name='search'),
    path('start/<str:game_name>', views.start_view, name='start'),
    path('accounts/<str:game_name>/', views.get_post_list, name='list'),
    # path('accounts/<str:game_name>/<str:id>/', views.get_post_detail, name='details'),
    path('accounts/<str:game_name>/<str:id>/site_index', views.get_post_detail, name='details'),

    path('<str:game_name>/', views.get_post_list, name='lists'),
    path('mmo-trading-market/<str:id>/', views.get_post_detail_by_id),
]
