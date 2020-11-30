from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include("blog.urls")),
    path('autenticacion/', include("autenticacion.urls")),
    path('', include("productos.urls")),
    path('carrito/', include("carrito.urls")),
    path('pedidos/', include("pedidos.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
