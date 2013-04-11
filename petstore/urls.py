from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
try:
    from django.views.generic.simple import direct_to_template
    home_page = (r'^$', direct_to_template, {'template': 'index.html'})
except ImportError:
    from django.views.generic import TemplateView
    home_page = (r'^$', TemplateView.as_view(template_name='index.html'))

admin.autodiscover()

urlpatterns = patterns('',
    home_page,
    # django admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if not settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve', {'document_root':settings.STATIC_ROOT, 'insecure':True} ),
        url(r'^media/(?P<path>.*)$', 'serve', {'document_root':settings.MEDIA_ROOT, 'insecure':True} ),
    )

