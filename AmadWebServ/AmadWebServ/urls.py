from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    	# Examples:
    	# url(r'^$', 'AmadWebServ.views.home', name='home'),
    	# url(r'^blog/', include('blog.urls')),
	url(r'^top_airports/', include('top_airports.urls')),
    	url(r'^admin/', include(admin.site.urls)),
	url(r'^top_airports_json/', include('top_airports_json.urls')),

)

