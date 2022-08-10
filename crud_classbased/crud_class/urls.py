from django.urls import path
from .views import AddRetrive,UpdateDelete
urlpatterns = [
    path('addretrive/',AddRetrive.as_view()),
    path('updatedelete/<int:pk>/',UpdateDelete.as_view()),
]