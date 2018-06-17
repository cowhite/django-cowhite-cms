from django.test import TestCase
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

from .models import *

import datetime


class Common(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user1 = User.objects.create_user(
            username= "user1", password= "a",
            email= "user1@example.com")
        for x in range(1, 23):
            Page.objects.create(
                title='This is page - %s' % x, content='<h1>Page content</h1>',
                author=self.user1, status='P')


class PageTestCase(Common):
    def test_page(self):
        first_page = Page.objects.first()
        url = reverse("django-cowhite-cms:page", args=[first_page.slug])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['page'].title, first_page.title)


