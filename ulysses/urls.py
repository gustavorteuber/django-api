from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from core.views import (
    ContatosViewSet,
    DolarViewSet,
    IndiceViewSet,
    MyTokenObtainPairView,
    UsuarioViewSet,
    BannerViewSet,
    saqViewSet,
    acoesViewSet,

)



from uploader.router import router as uploader_router



router = DefaultRouter()
router.register(r'contatos', ContatosViewSet)
router.register(r'dolar', DolarViewSet)
router.register(r'indice', IndiceViewSet)
router.register(r'acoes', acoesViewSet)
router.register(r'usuario', UsuarioViewSet)
router.register(r'banner', BannerViewSet)
router.register(r'saq', saqViewSet)







urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("media/", include(uploader_router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)