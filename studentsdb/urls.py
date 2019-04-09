from django.conf import settings
from django.conf.urls.static import static
from students.views import  students, groups, journal
from django.contrib import admin
from django.urls import re_path


urlpatterns = [

    # Admin URL's
    re_path(r'^admin/', admin.site.urls),

    # Students URL's
    re_path(r'^$', students.students_list, name='home'),
    re_path(r'^students/add/$', students.students_add, name='students_add'),
    re_path(r'^students/(?P<sid>\d+)/edit', students.students_edit, name='students_edit'),
    re_path(r'^students/(?P<sid>\d+)/delete', students.students_delete, name='students_delete'),

    # Groups URL's
    re_path(r'^groups/$', groups.groups_list, name='groups'),
    re_path(r'^groups/add/$', groups.groups_add, name='groups_add'),
    re_path(r'^groups/(?P<gid>\d+)/edit/$', groups.groups_edit, name='groups_edit'),
    re_path(r'^groups/(?P<gid>\d+)/delete/$', groups.groups_delete, name='groups_delete'),

    # Journal
    re_path(r'^journal/$', journal.journal, name='journal'),

]

if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





