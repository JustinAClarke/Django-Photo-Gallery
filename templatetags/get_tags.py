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
from django import template
from django.shortcuts import render
from photos.models import Photo, Tag


register = template.Library()

"""
#@register.inclusion_tag('photos/tags.html', takes_context=True)
#@register.tag
@register.filter(name='get_tags')
def get_tags(tags_query):
    tags=[]
    tag_str = "-"
    tag_list = list(tags_query)
    return tag_list
    for tag in tag_list:
        tags.append(tag)
    tag_str.join(tags)
    #return str(tags_query)
    return tags_str
    #categories = Category.objects.all().order_by('Title')
    #context = {'categories': categories}
 #   return render(request, 'recipes/categories_div.html', context)
    #return context
"""

@register.filter(name='get_tags')
def get_tags(photo_id):
    photo = Photo.objects.get(pk=photo_id)
    tags = []
    tag_str = " "
    for tag in photo.tags.all():
        tags.append(tag.title)
    #return str(tags_query)
    #return tag_str.join(tags)
    return tags
    
    #return tag_str
    #categories = Category.objects.all().order_by('Title')
    #context = {'categories': categories}
 #   return render(request, 'recipes/categories_div.html', context)
    #return context

