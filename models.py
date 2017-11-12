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

from django.db import models
from django.utils import timezone

# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

class Photo(models.Model):
    title = models.CharField(max_length=200)
    capture_date = models.DateField('Capture Date')
    description = models.TextField(null=True)
    tags = models.ManyToManyField(Tag)
    image_file = models.ImageField()
    
    def __str__(self):
        return self.title
