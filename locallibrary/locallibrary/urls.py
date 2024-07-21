
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from locallibrary import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='catalog/')),
]
# Add Django site authentication urls (for login, logout, password management)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
