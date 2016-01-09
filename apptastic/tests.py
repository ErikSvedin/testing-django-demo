from django.core.urlresolvers import resolve
from django.test import TestCase
from apptastic.views import home_page
from django.template.loader import render_to_string

from django.http import HttpRequest

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
