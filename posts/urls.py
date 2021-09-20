from django.urls import path
from . import views
from .views import image_upload_view, HomePageView

urlpatterns = [
    path('upload/', views.image_upload_view),
    path('', HomePageView.as_view(), name='home'),
    path('search/', views.search_results, name='search_results'),
    path("gallery/<int:pk>/", views.image_detail, name="image_detail"),
    path("gallery/", views.image_index, name="image_index"),
]
