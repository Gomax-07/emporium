from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from posts import views
from posts.views import success

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("django.contrib.auth.urls")),
    path('', include("users.urls")),
    path('posts/', include('posts.urls')),
    path('blog/', include('upposts.urls')),
    path("image/", views.home_view, name="home_view"),
    path('success', success, name='success'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)