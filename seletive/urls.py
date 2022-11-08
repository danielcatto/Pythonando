from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #na home/ não esqueça de informar a barra (/)
    path('admin/', admin.site.urls),
    path('home/', include('empresa.urls'))
]
