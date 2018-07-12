from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^tenant/$', views.tenant_homepage, name='tenant'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
