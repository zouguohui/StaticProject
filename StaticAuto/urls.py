from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name='index'),
    path('login.html', views.loginView, name='register'),
    path('logout.html', views.logoutView, name='logout'),
    path('fabitest.html', views.FabiTestView, name='fabitest'),
    path('fabipre.html', views.FabiPreView, name='fabipre'),
    path('sharertest.html', views.SharerTestView, name='sharertest'),
    path('sharerpre.html', views.SharerPreView, name='sharerpre'),
    path('bjbtest.html', views.BjbTestView, name='bjbtest'),
    path('bjbpre.html', views.BjbPreView, name='bjbpre'),
    path('bjbstatictest.html', views.BjbstaticTestView, name='bjbstatictest'),
    path('bjbstaticpre.html', views.BjbstaticPreView, name='bjbstaticpre'),
    path('sharerdev.html', views.SharerDevView, name='sharerdev'),
]
