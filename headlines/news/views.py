from django.views.generic import TemplateView
from users.models import Country, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from pprint import pprint
import requests
from news.tasks import get_response
# from django.shortcuts import render
# from django.http import JsonResponse


class IndexPageView(TemplateView, LoginRequiredMixin):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            if self.request.user.id in cache:
                result = cache.get(self.request.user.id)
            else:
                result = get_response(self.request.user)
            context['payload'] = result
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
