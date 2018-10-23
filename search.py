"""Search Page models."""
from django.conf import settings  # 1

from wagtail.core.models import Page  # 2

from algoliasearch import algoliasearch  # 3


#  4
class SearchPage(Page):
    """A search page class."""

    template = "cms/pages/search_page.html"

    class Meta:
        """Verbose names."""

        verbose_name = "Search Page"
        verbose_name_plural = "Search Pages"

    def get_context(self, request):
        """Algolia Searching. This view is used for page requests, not typing autocomplete."""
        context = super().get_context(request)
        query_string = request.GET.get("q") or False
        if query_string:
            client = algoliasearch.Client(
                settings.ALGOLIA.get("APPLICATION_ID"), settings.ALGOLIA.get("API_KEY")
            )
            algolia_index = client.init_index("test_index")
            context["results"] = algolia_index.search(query_string)
        return context
