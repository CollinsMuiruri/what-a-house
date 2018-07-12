from django.conf import settings
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    url(r'^$', views.welcome_page, name='welcome'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
