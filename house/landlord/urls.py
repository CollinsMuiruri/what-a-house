from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^landlord/$', views.landlord_homepage, name='landlord'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
