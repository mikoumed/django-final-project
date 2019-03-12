from django.test import TestCase
from users.models import User, Country, Category
import json

class UserEndpointTestCase(TestCase):

    def setUp(self):
        self.category1 = Category.objects.create(name='Entertainment')
        self.category2 = Category.objects.create(name='Sports')

        self.country1 = Country.objects.create(name='United States')
        self.country2 = Country.objects.create(name='France')

        self.user1 = User.objects.create_user(
        username='user1',
        email='user1@gmail.com',
        password='user1user1'
        )
        self.user1.categories.set([self.category1, self.category2])
        self.user1.countries.set([self.country1, self.country2])

        self.user2 = User.objects.create_user(
        username='user2',
        email='user2@gmail.com',
        password='user2user2'
        )
        self.user2.categories.set([self.category1, self.category2])
        self.user2.countries.set([self.country1, self.country2])



    def test_detail(self):
        response = self.client.get('/api/users/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-type'], 'application/json')
        expected = {
        'username':'user1',
        'email':'user1@gmail.com',
        'categories':[self.category1.name, self.category2.name],
        'countries':[self.country1.name,self.country2.name]
        }
        self.assertEqual(response.json(), expected)

    def test_list(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-type'], 'application/json')
        expected = [
        {
        'username':'user1',
        'email':'user1@gmail.com',
        'categories':[self.category1.name, self.category2.name],
        'countries':[self.country1.name, self.country2.name]
        },
        {
        'username':'user2',
        'email':'user2@gmail.com',
        'categories':[self.category1.name, self.category2.name],
        'countries':[self.country1.name, self.country2.name]
        }
        ]
        self.assertEqual(response.json(), expected)

    def test_create(self):
        self.assertEqual(User.objects.count(), 2)
        payload = {
        'username':'user3',
        'email':'user3@gmail.com',
        'password': 'user3user3',
        'categories':[self.category1.name],
        'countries':[self.country1.name]
        }
        json_payload = json.dumps(payload)
        response = self.client.post('/api/users/', data=json_payload, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(User.objects.count(), 3)

    def test_partial_update(self):
        payload = {'username': 'a_name'}
        json_payload = json.dumps(payload)

        response = self.client.patch(
            '/api/users/1/', data=json_payload, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.json()['username'], 'a_name')
        self.assertEqual(User.objects.get(id=1).username, 'a_name')

    def test_full_update(self):
        payload = {
        'username':'user4',
        'email':'user4@gmail.com',
        'password': 'user4user4',
        'categories':[self.category1.name],
        'countries':[self.country1.name]
        }
        json_payload = json.dumps(payload)

        response = self.client.put(
            '/api/users/1/', data=json_payload, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.json()['username'], 'user4')
        self.assertEqual(User.objects.get(id=1).username, 'user4')

    def test_delete(self):
        self.assertEqual(User.objects.count(), 2)
        response = self.client.delete('/api/users/1/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(User.objects.count(), 1)


    def test_invalid_json(self):
        json_payload = '[{"not a valid JSON": "not a valid JSON"}]'
        response = self.client.post(
            '/api/users/', data=json_payload, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.json(),
                         {
                            "non_field_errors": [
                            "Invalid data. Expected a dictionary, but got list."
                            ]})

    def test_create_with_invalid_country_and_category(self):
        payload = {
        'username':'user3',
        'email': 'user3@gmail.com',
        'password':'user3user3',
        'categories':['cat'],
        'countries':['cou']
        }
        json_payload = json.dumps(payload)

        response = self.client.post(
            '/api/users/', data=json_payload, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.json(),
                        {
                            "categories": [
                                "Object with name=cat does not exist."
                            ],
                            "countries": [
                                "Object with name=cou does not exist."
                            ]})

    def test_detail_invalid_method(self):
        response = self.client.post(
            '/api/users/1/', data='{}', content_type='application/json')
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.json(),
                         {"detail": "Method \"POST\" not allowed."})

    def test_list_invalid_method(self):
        response = self.client.delete('/api/users/', content_type='application/json')
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.json(),
                         {"detail": "Method \"DELETE\" not allowed."})


class CategoryEndpointTestCase(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name='category1')
        self.category2 = Category.objects.create(name='category2')


    def test_detail(self):
        response = self.client.get('/api/categories/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-type'], 'application/json')
        expected = {
        'name':'category1'
        }
        self.assertEqual(response.json(), expected)

    def test_list(self):
        response = self.client.get('/api/categories/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-type'], 'application/json')
        expected = [
        {
        'name':'category1',
        },
        {
        'name':'category2',
        }
        ]
        self.assertEqual(response.json(), expected)

    def test_create(self):
        self.assertEqual(Category.objects.count(), 2)
        payload = {
        'name':'category3',
        }
        json_payload = json.dumps(payload)
        response = self.client.post('/api/categories/', data=json_payload, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(Category.objects.count(), 3)

    def test_full_update(self):
        payload = {
        'name':'category3',
        }
        json_payload = json.dumps(payload)

        response = self.client.put(
            '/api/categories/1/', data=json_payload, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.json()['name'], 'category3')
        self.assertEqual(Category.objects.get(id=1).name, 'category3')

    def test_delete(self):
        self.assertEqual(Category.objects.count(), 2)
        response = self.client.delete('/api/categories/1/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Category.objects.count(), 1)

class CountryEndpointTestCase(TestCase):
    def setUp(self):
        self.category1 = Country.objects.create(name='country1')
        self.country2 = Country.objects.create(name='country2')


    def test_detail(self):
        response = self.client.get('/api/countries/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-type'], 'application/json')
        expected = {
        'name':'country1'
        }
        self.assertEqual(response.json(), expected)

    def test_list(self):
        response = self.client.get('/api/countries/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-type'], 'application/json')
        expected = [
        {
        'name':'country1',
        },
        {
        'name':'country2',
        }
        ]
        self.assertEqual(response.json(), expected)

    def test_create(self):
        self.assertEqual(Country.objects.count(), 2)
        payload = {
        'name':'country3',
        }
        json_payload = json.dumps(payload)
        response = self.client.post('/api/countries/', data=json_payload, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(Country.objects.count(), 3)

    def test_full_update(self):
        payload = {
        'name':'country3',
        }
        json_payload = json.dumps(payload)

        response = self.client.put(
            '/api/countries/1/', data=json_payload, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.json()['name'], 'country3')
        self.assertEqual(Country.objects.get(id=1).name, 'country3')

    def test_delete(self):
        self.assertEqual(Country.objects.count(), 2)
        response = self.client.delete('/api/countries/1/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Country.objects.count(), 1)
