from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # pour afficher la page login au debut de chaque demarage
    # path('', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
]
