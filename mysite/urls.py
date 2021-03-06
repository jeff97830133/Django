from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import welcome
from restaurants.views import menu, list_restaurants, comment


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^menu/$', menu),
	url(r'^welcome/$', welcome),
	url(r'^restaurants_list/$', list_restaurants),
	url(r'^comment/(\d{1,5})/$', comment),
)
