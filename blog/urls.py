from . import views
from django.urls import path
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('blogs', views.PostList.as_view(), name='blogs'),
    path('projects', views.projects, name='projects'),
    path('connect', views.connect, name='connect'),
]

# urlpatterns += staticfiles_urlpatterns()