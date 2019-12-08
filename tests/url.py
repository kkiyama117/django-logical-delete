import sys

from django.conf.urls import include

urlpatterns = [
]

if 'test' in sys.argv:
    from django.contrib import admin
    from django.urls import path

    admin.autodiscover()

    urlpatterns.append(path('admin/', admin.site.urls))
    urlpatterns.append(path('accounts/', include('django.contrib.auth.urls')))
