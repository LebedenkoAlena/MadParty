from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("app.api.urls")),
    path('', include("users.urls")),
    path('', include("app.urls")),
]
