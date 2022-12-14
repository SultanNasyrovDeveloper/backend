from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),

    path('api/v1/palace/', include('mind_palace.palace.node.urls')),
    path('api/v1/palace/', include('mind_palace.palace.urls')),
    path('api/v1/learning/sessions/', include('mind_palace.learning.session.urls')),
    path('api/v1/learning/statistics/', include('mind_palace.learning.statistics.urls')),
    path('api/v1/learning/', include('mind_palace.learning.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
