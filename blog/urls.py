from django.urls import path
from .views import PostView

urlpatterns = [
    path('post_view/', PostView.as_view(), name='post_view'),
]
