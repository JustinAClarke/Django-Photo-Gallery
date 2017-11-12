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

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.files import File

# Create your views here.


from .models import Photo, Tag
from .forms import *


def index(request):
    context = {'request': request}
    return render(request, 'photos/index.html', context)

def login(request):
    context = {'request': request}
    return render(request, 'photos/login.html', context)

def logout(request):
    return HttpResponseRedirect(reverse('photos:index'))

def admin_list(request):
    photos = Photo.objects.all().order_by('Title')
    tags = Tag.objects.all().order_by('Title')
    context = {'request': request,'photos':photos,'tags':tags}
    return render(request, 'photos/admin_list.html', context)


def add(request):
    if request.method == "POST":
        photo = PhotoForm(request.POST, request.FILES) # A form bound to the POST data
        if photo.is_valid(): # All validation rules pass
            new_photo = photo.save()
            return HttpResponseRedirect(reverse('photos:view_single', args=(new_photo.id)))
    else:
        photo = PhotoForm()
    context = {'request': request,'form':photo}
    return render(request, 'photos/add.html', context)

def edit(request,id):
    photo = get_object_or_404(Photo, pk=id)
    if request.method == "POST":
        photo = PhotoForm(request.POST) # A form bound to the POST data
        if photo.is_valid(): # All validation rules pass
            new_photo = photo.save()
            return HttpResponseRedirect(reverse('photos:view_single', args=(new_photo.id)))
    else:
        photo = PhotoForm()
    context = {'request': request,'form':photo}
    return render(request, 'photos/add.html', context)
    
def add_tag(request):
    if request.method == "POST":
        tag = TagForm(request.POST) # A form bound to the POST data
        if tag.is_valid(): # All validation rules pass
            new_tag = tag.save()
            return HttpResponseRedirect(reverse('photos:add_tag'))
    else:
        tag = TagForm()
    context = {'request': request,'form':tag}
    return render(request, 'photos/add.html', context)
    
def edit_tag(request,id):
    tag = get_object_or_404(Tag, pk=id)
    if request.method == "POST":
        tag = TagForm(request.POST) # A form bound to the POST data
        if tag.is_valid(): # All validation rules pass
            new_tag = tag.save()
            return HttpResponseRedirect(reverse('photos:add_tag'))
    else:
        tag = TagForm()
    context = {'request': request,'form':tag}
    return render(request, 'photos/add.html', context)

def view_single(request,id):
    photo = get_object_or_404(Photo, pk=id)
    context = {'request': request,'photo':photo}
    return render(request, 'photos/view_single.html', context)

def view_all(request):
    photos = Photo.objects.all().order_by('Title')
    context = {'request': request,'photos':photos}
    return render(request, 'photos/view_all.html', context)



def preview(request,id):
    photo = get_object_or_404(Photo, pk=id)
    #photo_file = open(photo.image_file)
    return photo.image_file.open()

def test(request,id):
    context = {'request': request}
    return render(request, 'photos/test.html', context)
