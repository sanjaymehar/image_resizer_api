from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from task.views import *
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
router = routers.DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
#    path('', include(router.urls)),
    path('',YourModelView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
