from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class IndexPageView(TemplateView):
    template_name = 'index.html'
    # newsapi = NewsApiClient(api_key='d380b7d83c074b4e8b710d302cc53601')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            categories = self.request.user.categories
            languages = self.request.user.languages
            countries = self.request.user.countries

        #
        # for category in categories:
        #     response = newsapi.get_top_headlines(category=category)
