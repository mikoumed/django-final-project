from django.shortcuts import render
from django.views.generic import TemplateView
import requests
from users.models import Country, Category
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime, timedelta

COUNTRIES = {
    'United States' : 'us',
    'France' : 'fr',
    'Australia' : 'au',
    'Great Britain': 'gb',
    'Germany' : 'de'
}

class IndexPageView(TemplateView, LoginRequiredMixin):
    template_name = 'index.html'
    news_api_key = 'd380b7d83c074b4e8b710d302cc53601'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            categories = self.request.user.categories.all()
            countries = self.request.user.countries.all()
            results = {}
            def request_api():
                for country in countries:
                    results.setdefault(country.name, {})
                    for category in categories:
                        try:
                            response = requests.get('https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={api_key}'.format(
                                        country=COUNTRIES[country.name], category=category.name, api_key=self.news_api_key)).json()
                        except requests.exceptions.RequestException as e:
                            return e

                        results[country.name].setdefault(category.name,[])
                        results[country.name][category.name] = response['articles']
                context['payload'] = results
                self.request.session['last_result'] = results
                self.request.session['last_time'] = datetime.now().strftime('%H%M%S')

            if 'last_time' not in self.request.session:
                request_api()
            elif datetime.now() - datetime.strptime(self.request.session['last_time'] ,'%H%M%S') <= timedelta(minutes=15):
                request_api()
            else:
                context['payload'] = self.request.session['last_result']
            return context

# def json_response(request):
#     categories = Category.objects.all()
#     countries = Country.objects.all()
#     context = {}
#     for country in countries:
#         context.setdefault(country.name, {})
#         for category in categories:
#             try:
#                 response = requests.get('https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={api_key}'.format(
#                             country=COUNTRIES[country.name], category=category.name, api_key='d380b7d83c074b4e8b710d302cc53601')).json()
#             except requests.exceptions.RequestException as e:
#                 return e
#
#             context[country.name].setdefault(category.name,[])
#             context[country.name][category.name] = response['articles']
#     return JsonResponse(context, safe=False)
