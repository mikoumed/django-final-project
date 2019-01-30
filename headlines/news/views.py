from django.shortcuts import render
from django.views.generic import TemplateView
import requests
from users.models import Language, Category
from django.http import JsonResponse

# Create your views here.
COUNTRIES = {
    'english' : 'us',
    'french' : 'fr',
    'spanish' : 'sa'
}

class IndexPageView(TemplateView):
    template_name = 'index.html'
    news_api_key = 'd380b7d83c074b4e8b710d302cc53601'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            categories = self.request.user.categories.all()
            languages = self.request.user.languages.all()
            results = {}
            for language in languages:
                results.setdefault(language.name, {})
                for category in categories:
                    try:
                        response = requests.get('https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={api_key}'.format(
                                    country=COUNTRIES[language.name], category=category.name, api_key='d380b7d83c074b4e8b710d302cc53601')).json()
                    except requests.exceptions.RequestException as e:
                        return e

                    results[language.name].setdefault(category.name,[])
                    results[language.name][category.name] = response['articles']
            context['payload'] = results
            return context

def json_response(request):
    categories = Category.objects.all()
    languages = Language.objects.all()
    context = {}
    for language in languages:
        context.setdefault(language.name, {})
        for category in categories:
            try:
                response = requests.get('https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={api_key}'.format(
                            country=COUNTRIES[language.name], category=category.name, api_key='d380b7d83c074b4e8b710d302cc53601')).json()
            except requests.exceptions.RequestException as e:
                return e

            context[language.name].setdefault(category.name,[])
            context[language.name][category.name] = response['articles']
    return JsonResponse(context, safe=False)
        #
        # for category in categories:
        #     response = newsapi.get_top_headlines(category=category)
