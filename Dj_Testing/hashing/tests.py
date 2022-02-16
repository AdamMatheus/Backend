from django.test import TestCase
from selenium import webdriver
from .forms import HashForm
import hashlib
from .models import Hash

class UnitTestCase(TestCase):
    def hashSave(self):
        hash = Hash()
        hash.text = 'hi'
        hash.hash = '8f434346648f6b96df89dda901c5176b10a6d83961dd3c1ac88b59b2dc327aa4'
        hash.save()
        return hash
    
    def test_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'hashing/home.html')
        
    def test_hash_form(self):
        form = HashForm(data={'text': 'hello'})
        self.assertTrue(form.is_valid())
        
    def test_hash_function_works(self):
        hash = hashlib.sha256('hello'.encode('utf-8')).hexdigest()
        self.assertEqual('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', hash)        
      
    def test_hash_model_object(self):
        hash = self.hashSave()
        pulled_hash = Hash.objects.get(hash='8f434346648f6b96df89dda901c5176b10a6d83961dd3c1ac88b59b2dc327aa4')
        self.assertEqual(hash.text, pulled_hash.text)
        
    def test_viewing_hash(self):
        hash = self.hashSave()
        response = self.client.get('/hash/8f434346648f6b96df89dda901c5176b10a6d83961dd3c1ac88b59b2dc327aa4')
        self.assertContains(response, 'hi')


class FunctionalTestCase(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
    
    def test_there_is_homepage(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Enter hash here', self.browser.page_source)
    
    def test_hash_of_hello(self):
        self.browser.get('http://localhost:8000')
        text = self.browser.find_element_by_id('id_text')
        text.send_keys('hello')
        self.browser.find_element_by_name("submit").click()
        self.assertInHTML('61be55a8e2f6b4e172338bddf184d6dbee29c98853e0a0485ecee7f27b9af0b4', self.browser.page_source)
    
    def tearDown(self):
        self.browser.quit()
