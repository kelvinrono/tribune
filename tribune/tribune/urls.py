
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('news.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logout/$', views.logout, {"next_page": '/'}),
    url(r'^tinymce/', include('tinymce.urls')),

]

