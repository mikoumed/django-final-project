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
            categories = self.request.user.categories.all()
            languages = self.request.user.languages.all()
            result = {}
            for category in categories:
                try:
                    response = requests.get('https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={api_key}'.format(
                                country='us', category=category.name, api_key='d380b7d83c074b4e8b710d302cc53601')).json()
                except requests.exceptions.RequestException as e:
                    return e

                result[category.name] = response['articles']
            context['articles'] = result

        return context
        #
        # for category in categories:
        #     response = newsapi.get_top_headlines(category=category)
