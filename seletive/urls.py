from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #na home/ não esqueça de informar a barra (/)
    path('admin/', admin.site.urls),
    path('home/', include('empresa.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)