
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('blog/', views.HomeView.as_view(), name = 'blog-name'),
    path('blog/entry/<int:pk>/', views.EntryView.as_view(), name = "entry-detail"),
    path('blog/create_entry/', views.CreateEntryView.as_view(success_url="/blog/"), name = "create_entry"),
    path('blog/entry/edit/<int:pk>/', views.UpdatePostView.as_view(success_url="/blog/"), name = "update_post"),
    path('blog/entry/<int:pk>/remove', views.DeletePostView.as_view(success_url="/blog/"), name = "delete_post")

]