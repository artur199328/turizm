from django.urls import path
from .views import  HomeListView,AboutListView,HotelListView,BlogListView, register_request, login_request,logout_request, HomePageDetailView
from . import views


urlpatterns = [
    path('', HomeListView.as_view(), name='index'),
    path('<int:id>/', HomePageDetailView.as_view(), name='index_detail'),
    path('about/', AboutListView.as_view(), name='about'),
    path('hotel/', HotelListView.as_view(), name='hotel'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('register/', register_request, name='register'),
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name = 'logout'),
    path('trichq/', views.trichq, name='trichq'),
    path('comment/', views.comment, name='comment')
]