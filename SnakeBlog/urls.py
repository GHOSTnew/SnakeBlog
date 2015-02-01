from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import ArticleFeed, ArticleSitemap, PageSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'blog': ArticleSitemap,
    'page': PageSitemap,
#    'page': GenericSitemap(pageInfo, priority=0.6),
}


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.home'),
    url(r'^post/(?P<name>[^/]+)/$', 'blog.views.getArticle', name='article-page'),
    url(r'^page/(?P<name>[^/]+)/$', 'blog.views.getPage', name='blog-page'),
    url(r'^feed/$', ArticleFeed()),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap')
)
