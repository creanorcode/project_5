from django.contrib.sitemaps import Sitemap

from products.models import Product


class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return getattr(obj, "created_at", None)


sitemaps = {"products": ProductSitemap}
