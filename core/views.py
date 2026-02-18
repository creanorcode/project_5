from django.http import HttpResponse


def robots_txt(request):
    """Serve a simple robots.txt file for SEO indexing."""
    return HttpResponse(
        "User-agent: *\nDisallow:\nSitemap: /sitemap.xml\n",
        content_type="text/plain"
    )
