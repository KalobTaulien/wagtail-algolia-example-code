"""Basic Wagtail Page."""
from wagtail.core.models import Page


class BasicPage(Page):
    """A basic page class."""

    template = "cms/pages/basic_page.html"  # Because I enjoy being verbose

    class Meta:
        """Verbose names."""

        verbose_name = "Basic Page"
        verbose_name_plural = "Basic Pages"
