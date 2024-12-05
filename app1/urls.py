from django.urls import path 
from . import views

# URL Config
urlpatterns = [
    # Blog list view
    path('blog/', views.blog_list, name='blog_list'),
    # Blog list Details    
    path('blog/<int:id>/', views.blog_details, name='blog_details'),
]