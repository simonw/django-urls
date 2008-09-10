from django.db import models
from django_urls.base import UrlMixin

"""
>>> article = ArticleWithPathDefined.objects.create(slug = 'my-article')
>>> article.get_url()
'http://localhost/articles/my-article/'
>>> article.get_url_path()
'/articles/my-article/'
>>> asset = AssetWithUrlDefined.objects.create(domain='example.com', filename='logo.png')
>>> asset.get_url()
'http://example.com/assets/logo.png'
>>> asset.get_url_path()
'/assets/logo.png'
"""

class ArticleWithPathDefined(models.Model, UrlMixin):
    slug = models.SlugField()
    
    def get_url_path(self):
        return '/articles/%s/' % self.slug

class AssetWithUrlDefined(models.Model, UrlMixin):
    domain = models.CharField(max_length=30)
    filename = models.CharField(max_length = 30)
    
    def get_url(self):
        return 'http://%s/assets/%s' % (self.domain, self.filename)
