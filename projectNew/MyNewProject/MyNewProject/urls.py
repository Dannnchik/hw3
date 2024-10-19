from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from MyNewProject.myapp import admin
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),  # Убедитесь, что имя 'myapp' совпадает с названием папки приложения
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
