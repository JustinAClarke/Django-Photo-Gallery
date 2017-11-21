## Getting Started With Django

### Create a python Virtual Enviropment
`python -m venv pyEnv`

### Step into pyEnv:
`source pyEnv/bin/activate`

###Install django and Pillow (image Editing):
`pip install django pillow`

###Create a Django site:
`django startsite DjangoPhotos`

###change directory into DjangoPhotos and clone Django-Photo-Gallery git repo:
`cd DjangoPhotos
git clone https://github.com/JustinFuhrmeister-Clarke/Django-Photo-Gallery.git photos`

###add urls and install Django-Photo-Gallery:
 * edit DjangoPhotos/settings.py and add the following line:
`    'photos.apps.PhotosConfig',`

 * edit DjangoPhotos/urls.py and add the following lines:
 `from django.conf.urls import include, url`
 `    url(r'^photos/', include('photos.urls')),`
 
###create database (default sqlite, in site root dir):
`./manage migrate`

###Start the site with:
`./manage runserver`
