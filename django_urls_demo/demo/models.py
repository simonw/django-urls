from django.db import models
from django_urls.base import UrlMixin

class PathDefined(models.Model, UrlMixin):
    slug = models.SlugField()
    
    def get_url_path(self):
        return '/blah/%s/' % self.slug

class UrlDefined(models.Model, UrlMixin):
    domain = models.CharField(max_length=30)
    
    def get_url(self):
        return 'http://%s/info.html' % self.domain
