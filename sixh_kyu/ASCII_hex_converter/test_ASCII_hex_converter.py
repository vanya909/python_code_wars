from unittest import TestCase
from ASCII_hex_converter import Converter

class TestConverter(TestCase):
    def test_to_ascii(self):
        self.assertEqual(Converter.to_ascii('4c6f6f6b2c20486172727921'), 'Look, Harry!')
        self.assertEqual(Converter.to_ascii('48656c6c6f2c206d79207665727920676f6f6420667269656e64'),
                         'Hello, my very good friend')
        self.assertEqual(Converter.to_ascii('20'), ' ')
        self.assertEqual(Converter.to_ascii(''), '')

    def test_to_hex(self):
        self.assertEqual(Converter.to_hex('Look, Harry!'), '4c6f6f6b2c20486172727921')
        self.assertEqual(Converter.to_hex('Hello, my very good friend'),
                         '48656c6c6f2c206d79207665727920676f6f6420667269656e64')
        self.assertEqual(Converter.to_hex(' '), '20')
        self.assertEqual(Converter.to_hex(''), '')
