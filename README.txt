Experimental replacement for Django's get_absolute_url method, as described on 
http://code.djangoproject.com/wiki/ReplacingGetAbsoluteUrl

For the moment I've implemented it as a mixin class. Here's how you use it::

    from django.db import models
    from django_urls.base import UrlMixin

    class ArticleWithPathDefined(models.Model, UrlMixin):
        slug = models.SlugField()
    
        def get_url_path(self):
            return '/articles/%s/' % self.slug

    class AssetWithUrlDefined(models.Model, UrlMixin):
        domain = models.CharField(max_length=30)
        filename = models.CharField(max_length = 30)
    
        def get_url(self):
            return 'http://%s/assets/%s' % (self.domain, self.filename)

You need to define either get_url_path or get_url on a model - there's no need 
to define both. If you define one, the other will magically start working. 
Here's an example session using the above models::

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
