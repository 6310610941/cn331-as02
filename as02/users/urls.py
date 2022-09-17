from django.urls import path, include

from . import views

app_name= 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('courses/', include('courses.urls')),
    path('regist', views.regist, name='regist'),
    path('remove', views.remove, name='remove'),
    path('book/', views.book, name='book'),
    path('<user_id>/book/', views.book, name='book'),
    path('<user_id>/delete/', views.delete, name='delete'),
    path('<user_id>/result', views.result, name='result'),
]