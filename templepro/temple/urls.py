from django.urls import path
from .views import Add_temple, List_temple, Delete_temple, Update_temple, Detail_temple

urlpatterns = [
    path('add/', Add_temple.as_view()),
    path('list/', List_temple.as_view()),
    path('detail/<int:pk>/', Detail_temple.as_view()),
    path('update/<int:pk>/', Update_temple.as_view()),
    path('delete/<int:pk>/', Delete_temple.as_view()),
]
