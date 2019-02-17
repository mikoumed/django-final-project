from django.core.cache import cache
from users.models import Category, Country, User
import requests
from celery import shared_task


COUNTRIES = {
    'United States' : 'us',
    'France' : 'fr',
    'Australia' : 'au',
    'Great Britain': 'gb',
    'Germany' : 'de'
}

def formatted_response(articles):
    result = []
    for article in articles:
        a_dict = {}
        new_value = ''
        for key, value in article.items():
            if key == 'content' and value:
                if '[' in value:
                    new_value = value[:value.index('[')]
                    a_dict[key] = new_value
                else:
                    a_dict[key] = value
            if key in ['url','source','title']:
                a_dict[key] = value
        result.append(a_dict)
    return result

def get_response(user):
    results = {}
    connect_timeout, read_timeout = 5.0, 30.0
    categories = user.categories.all()
    countries = user.countries.all()
    news_api_key = 'd380b7d83c074b4e8b710d302cc53601'
    for country in countries:
        results.setdefault(country.name, {})
        for category in categories:
            try:
                response = requests.get('https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={api_key}'.format(
                            country=COUNTRIES[country.name], category=category.name, api_key=news_api_key), timeout=(connect_timeout, read_timeout)).json()
            except requests.exceptions.RequestException as e:
                return e

            results[country.name].setdefault(category.name,[])
            results[country.name][category.name] = formatted_response(response['articles'])
    return results

@shared_task
def request_api():
    users = User.objects.all()
    for user in users:
        result = get_response(user)
        cache.set(user.id, result, timeout=None)
    return result
