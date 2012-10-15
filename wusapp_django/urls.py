from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wusapp_django.views.home', name='home'),
     url(r'^$', include('surftrain.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)



if settings.DEBUG:
    # add one of these for every non-static root you want to serve
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # this take cares of static media (i.e. bundled in apps, and specified in settings)
    urlpatterns+= staticfiles_urlpatterns()
