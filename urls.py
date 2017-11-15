"""
    Django Photo Gallery Justin Fuhrmeister-Clarke, a photo gallery based in django.
    Copyright (C) 2017  Justin Fuhrmeiser-Clarke <justin@fuhrmeister-clarke.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    """

from django.conf.urls import url

from . import views

app_name = 'photos'

urlpatterns = [
    # ex: /photos/
    url(r'^$', views.index, name='index'),
    
    # ex: /photos/login
    url(r'^login/$', views.login, name='login'),
    
    # ex: /photos/logout
    url(r'^logout/$', views.logout, name='logout'),
    
    #admin list photos/tags
    # ex: /photos/admin_list/
    url(r'^admin_list/$', views.admin_list, name='admin_list'),
    
    #add/edit photos
    # ex: /photos/add/
    url(r'^add/$', views.add, name='add'),
    
    # ex: /photos/edit/
    url(r'^edit/(?P<id>[0-9]+)/$', views.edit, name='edit'),
    
    #add/edit tags
    # ex: /photos/add/tag
    url(r'^add/tag/$', views.add_tag, name='add_tag'),
    
    # ex: /photos/edit/tag
    url(r'^edit/tag/(?P<id>[0-9]+)/$', views.edit_tag, name='edit_tag'),
    
    #view
    # ex: /photos/view/id/
    url(r'^view/(?P<id>[0-9]+)/$', views.view_single, name='view_single'),
    
    # ex: /photos/view/
    url(r'^view/$', views.view_all, name='view_all'),
    
    # ex: /photos/preview/
    url(r'^preview/(?P<id>[0-9]+)/$', views.preview, name='preview'),
    
    # ex: /photos/thumbnail/
    url(r'^thumbnail/(?P<id>[0-9]+)/$', views.thumbnail, name='thumbnail'),
    
    # ex: /photos/original/
    url(r'^original/(?P<id>[0-9]+)/$', views.original, name='original'),
    
    # ex: /photos/reload_previews/
    url(r'^reload_previews/$', views.reload_previews, name='reload_previews'),
    
    url(r'^test/(?P<recipe>[0-9]+)/$', views.test, name='test'),
    
]
