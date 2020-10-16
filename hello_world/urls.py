from django.urls import path
from hello_world import views

urlpatterns = [
    path('', views.hello_world, name='hello_worlds'),
    path('contact', views.my_contact, name='my_contacts'),
    path('service', views.my_service, name='my_services'),
    path('portfolio', views.my_portfolio, name='my_portfolios'),
    path('about', views.my_about, name='my_abouts'),
    path('blog', views.my_blog, name='my_blogs'),
    path('blog/blog_single', views.my_blog_single, name='my_blog_singles'),
]
