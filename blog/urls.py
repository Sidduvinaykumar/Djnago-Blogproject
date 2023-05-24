from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="blog-home"),
    path("about/", views.about, name="blog-about"),
    path("admin/blog/post/add/", views.Createpost, name="blog-Createpost"),
]
