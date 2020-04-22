from django.test import TestCase
from django.urls import reverse


class CoreViewTestCase(TestCase):
    def test_home(self):
        resp = self.client.get(reverse('core:home'))
        self.assertEqual(resp.status_code, 200)
