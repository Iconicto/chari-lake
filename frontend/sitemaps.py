from django.contrib import sitemaps
from django.urls import reverse
from .urls import urlpatterns

paths = []

for path in urlpatterns:
    paths.append(path.name)


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return paths

    def location(self, item):
        return reverse(item)
