from SnakeBlog.utils.render import custom_render
from django.http import Http404
from blog.models import Article, Page, Comment
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from blog.forms import commentForm
from django.contrib import sitemaps
from django.core.context_processors import csrf


class ArticleFeed(Feed):
    link = "/feed/"

    def items(self):
        return Article.objects.order_by('-date')

    def item_title(self, obj):
        return obj.title

    def item_description(self, obj):
        return obj.content_html

    def item_link(self, obj):
        return reverse('article-page', args=(obj.title,))


class ArticleSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Article.objects.order_by('-date')

    def location(self, obj):
        return reverse('article-page', args=(obj.title,))


class PageSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Page.objects.all()

    def location(self, obj):
        return reverse('blog-page', args=(obj.title,))


def home(request):
    Article_list = Article.objects.order_by('-date')
    paginator = Paginator(Article_list, 5)
    page = request.GET.get('page')
    try:
        art = paginator.page(page)
    except:
        art = paginator.page(1)
    return custom_render('index.html', {'Article': art})


def getArticle(request, name):
    try:
        art = Article.objects.get(title=name)
        try:
            com = Comment.objects.filter(Article=art)
        except:
            com = None
    except Exception:
        raise Http404
    context = {'Article': art, 'Comments': com, 'Form': commentForm()}
    context.update(csrf(request))
    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            titre = form.cleaned_data['title']
            content = form.cleaned_data['content']
            author = form.cleaned_data['author']
            email = form.cleaned_data['authorEmail']
            Comment(title=titre, Article=art, content=content, author=author, authorEmail=email).save()
        else:
            context['error'] = True
    return custom_render('article.html', context)


def getPage(request, name):
    try:
        pa = Page.objects.get(title=name)
    except Exception:
        raise Http404
    return custom_render('page.html', {'Page': pa})
