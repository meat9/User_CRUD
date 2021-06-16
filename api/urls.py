from django.urls import include, path
from . import views

urlpatterns = [
    path("create_auth/", views.create_auth),  # Создание юзера
    path("get_all_users/", views.get_all_users),  # список юзеров
    path("get_user/", views.get_user),  # получить юзера
    path("put_user/<int:id>", views.put_user),
    path("patch_user/<int:id>", views.patch_user),
    path("delete_user/<int:id>", views.delete_user),
]
