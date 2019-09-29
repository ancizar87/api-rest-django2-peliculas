from django.contrib import admin
from django.urls import path, include

from api import views
from rest_framework import routers

router = routers.DefaultRouter()

# En el router añadimos los endpoints a los viewsets
router.register('peliculas', views.PeliculaViewSet)

urlpatterns = [
  path('api/v1/', include(router.urls)),
  path('api/v1/favorita/', views.MarcarPeliculaFavorita.as_view()),
  path('api/v1/favoritas/', views.ListarPeliculasFavoritas.as_view()),
  path('admin/', admin.site.urls),
  path('api/v1/auth/', include('rest_auth.urls')),
  path('api/v1/auth/registration/', include('rest_auth.registration.urls')),
]