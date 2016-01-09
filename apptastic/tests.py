from django.core.urlresolvers import resolve
from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

from apptastic.views import home_page
from django.template.loader import render_to_string

from django.http import HttpRequest

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

class HomePageFunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(HomePageFunctionalTest, cls).setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(HomePageFunctionalTest, cls).tearDownClass()


    def test_site_is_about_drone(self):
        # Visit app
        self.selenium.get('%s%s' % (self.live_server_url, '/'))

        # Expect webpage to be about drone
        self.assertIn('Webpage about drone', self.selenium.title)
