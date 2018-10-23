# admin.py
# Register Wagtail models with Algolia search

from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .basic import BasicPage


@register(BasicPage)
class BasicPageIndex(AlgoliaIndex):
    """Register Basic Page Index with Algolia."""

    fields = ("title", "seo_title", "search_description")  # *This field becomes import now!*
    settings = {
        "searchableAttributes": [
            "title",
            "seo_title",
            "search_description",
        ]
    }
    index_name = 'test_index'  # This is the name of the index from the image above. 