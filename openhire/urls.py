from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from users.views import register_user

urlpatterns = [
    path('admin/', admin.site.urls),
    #USERS
    path('register/', register_user, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)