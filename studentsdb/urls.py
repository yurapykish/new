"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from students import students_views,groups_views, journal_views, ekzam_views,contact_admin_views
from django.conf.urls.static import static
from django.conf import settings
from .settings import MEDIA_ROOT, DEBUG



urlpatterns = [
    # students url
    url(r'^$', students_views.students_list, name ='home'),
    url(r"^students/add/$", students_views.students_add, name="students_add"),
    url(r"^students/(?P<sid>\d+)/edit/$", students_views.students_edit, name="students_edit"),
    url(r"^students/(?P<sid>\d+)/delete/$", students_views.students_delete, name="students_delete"),

    # groups url
    url(r'^groups/$', groups_views.groups_list, name ='groups'),
    url(r"^groups/add/$", groups_views.groups_add, name="groups_add"),
    url(r"^groups/(?P<gid>\d+)/edit/$", groups_views.groups_edit, name="groups_edit"),
    url(r"^groups/(?P<gid>\d+)/delete/$", groups_views.groups_delete, name="groups_delete"),

    #journal url
    url(r'^journal/$', journal_views.journal, name = 'journal'),
	url(r'^ekzam/$', ekzam_views.ekzam, name ='ekzam'),
	url(r'^ekzam_add/$', ekzam_views.ekzam_add, name = 'ekzam_add'),

	url(r'^contact_admin/$', contact_admin_views.contact_admin, name='contact_admin'),
    url(r'^admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    #serve files from media folder
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

