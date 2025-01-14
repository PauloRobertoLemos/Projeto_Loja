from django.urls import path
from .views import create_produto, update_produto, produto_list, delete_produto


urlpatterns = [
    path('', produto_list, name="list"), 
    path('create/', create_produto, name="create"),
    path('update/<int:pk>', update_produto, name="update"),
    path('delete/<int:pk>', delete_produto, name="delete")
]