from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('category/', category, name='category'),
    path('contact/', contact, name='contact'),
    path('details/', details, name='details'),
    path('elements/', elements, name='elements'),
    path('latest_news/', latest_news, name='latest_news'),
    path('main/', main, name='main'),
    path('single-blog/', single_blog, name='single-blog'),

]

