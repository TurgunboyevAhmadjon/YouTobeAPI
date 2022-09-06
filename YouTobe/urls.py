from django.contrib import admin
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from asosiy.views import *

schema_view = get_schema_view(
   openapi.Info(
      title="YouTobeAPI",
      default_version='v1',
      description="Test description",
      # terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      # license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pleylist/', PleylistView.as_view()),
    path('account/', AccountView.as_view()),
    path('obuna/', ObunaView.as_view()),
    path('like/', LikeView.as_view()),
    path('history/', HistoryView.as_view()),
    path('video/', VideoView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
