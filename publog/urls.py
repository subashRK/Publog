from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.views.generic.base import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="all_posts"), name="home"),
    path('admin/', admin.site.urls),
    path("user/", include("users.urls")),
    path("post/", include("posts.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
