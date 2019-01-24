from django.shortcuts import render
from django.views.generic import TemplateView
import requests

# Create your views here.

class IndexPageView(TemplateView):
    template_name = 'index.html'
    news_api_key = 'd380b7d83c074b4e8b710d302cc53601'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            categories = self.request.user.categories
            languages = self.request.user.languages
            
        try:
            response = requests.get('https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'.format(country='us', api_key='d380b7d83c074b4e8b710d302cc53601')).json()
        except requests.exceptions.RequestException as e:
            return e

        context['count'] = response['totalResults']
        context['articles'] = response['articles']

        return context
        #
        # for category in categories:
        #     response = newsapi.get_top_headlines(category=category)
