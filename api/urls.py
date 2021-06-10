from django.urls import include, path
from . import views

urlpatterns = [
  #path('welcome/', views.welcome),
  path('create_auth/', views.create_auth), #Создание юзера
  path('get_all_users/', views.get_all_users), #список юзеров
  path('get_user/', views.get_user),# получить юзера
  path('put_user/<int:id>', views.put_user),
  path('patch_user/<int:id>', views.patch_user),
  path('delete_user/<int:id>', views.delete_user),


#   path('addbook/', views.add_book),
#   path('updatebook/<int:book_id>', views.update_book),
#   path('deletebook/<int:book_id>', views.delete_book),
#   path('register/', views.create_auth),

]