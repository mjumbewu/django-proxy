from django.test import TestCase
from proxy.views import make_absolute_location


class TestAbsoluteLocation(TestCase):
    def test_already_absolute(self):
        absurl = make_absolute_location(
            'https://example.com/test/path',
            'https://example2.com/next/test/path?with=qs')
        self.assertEquals(absurl, 'https://example2.com/next/test/path?with=qs')

    def test_scheme_relative(self):
        absurl = make_absolute_location(
            'https://example.com/test/path',
            '//example2.com/next/test/path?with=qs')
        self.assertEquals(absurl, 'https://example2.com/next/test/path?with=qs')

    def test_host_relative(self):
        absurl = make_absolute_location(
            'https://example.com/test/path',
            '/next/test/path?with=qs')
        self.assertEquals(absurl, 'https://example.com/next/test/path?with=qs')

    def test_path_relative(self):
        absurl = make_absolute_location(
            'https://example.com/test/path',
            'next/test/path?with=qs')
        self.assertEquals(absurl, 'https://example.com/test/next/test/path?with=qs')
