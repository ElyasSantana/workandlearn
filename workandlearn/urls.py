from django.contrib import admin
from django.urls import path, include
from .routers import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include(empresa_router.urls)),
    path('api/', include(dev_router.urls)),
]
