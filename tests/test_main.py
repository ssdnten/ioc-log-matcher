import unittest
from main import match,normalize

class Tests(unittest.TestCase):
    def test_domain_normalization(self): self.assertEqual(normalize('domain','DEMO.EXAMPLE.'),'demo.example')
    def test_exact_not_substring(self): self.assertEqual(match([dict(type='domain',value='demo.example')],[dict(domain='notdemo.example')]),[])
    def test_ipv6(self): self.assertEqual(len(match([dict(type='ip',value='2001:db8::1')],[dict(ip='2001:0db8:0:0:0:0:0:1')])),1)
    def test_multiple_labels(self): self.assertEqual(match([dict(type='ip',value='192.0.2.1',label='b'),dict(type='ip',value='192.0.2.1',label='a')],[dict(ip='192.0.2.1')])[0]['labels'],['a','b'])
    def test_missing_fields(self): self.assertEqual(match([], [dict(message='demo')]),[])
    def test_bad_ip(self):
        with self.assertRaises(ValueError): normalize('ip','999.1.1.1')
    def test_bad_domain(self):
        with self.assertRaises(ValueError): normalize('domain','a..example')
