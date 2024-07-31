from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    #path to see admin screen 管理画面へのパス
    path('admin/', admin.site.urls),

    path('', views.home, name='index'),

    path('sign_out/', views.sign_out, name='sign_out'),

    path('view/sign-in.html', views.sign_in, name='sign_in'),

    path('view/sign-up.html', views.sign_up, name='sign_up'),

    path('view/index-logined.html', views.index_logined, name='index_logined'),

    path('view/view-homework.html', views.view_homework, name='view_homework'),

    path('view/add-homework.html', views.add_homework, name='add_homework'),

    path('view/homework-details.html/<int:id>/', views.homework_details, name='homework_details'),

    path('view/finished-homework.html', views.finished_homework, name='finished_homework'),

    path('delete_homework/', views.delete_homework, name='delete_homework')
]