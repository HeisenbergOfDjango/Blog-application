from django.urls import path
from .views import *


app_name = 'blog'


urlpatterns = [
    path('', post_list, name='post-view'),
    path('<int:id>/', post_details, name='post-deatils')
]
