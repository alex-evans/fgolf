from django.urls import path

from . import views

app_name = 'tournaments'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:tournament_id>/', views.detail, name='detail'),
    path('<int:tournament_id>/make_picks', views.make_picks, name='make_picks')
]