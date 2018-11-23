# -*- coding: utf-8 -*-
"""
Created on Wed Nov 7 21:49:55 2018

@author: Umar Bin Khalid
"""

from django.test import TestCase
from django.urls import resolve, reverse
from CrudAssignment.views import index, retrieve
# Create your tests here.

"""
    @author: Umar Bin Khalid
"""
class HomePageTest(TestCase):

    """
    @author: Umar Bin Khalid
    """
    def test_resolves_to_index_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    """
    @author: Umar Bin Khalid
    """
    def test_retrieve_url(self):
        print("Karmjit Kaur")
        response = self.client.get(reverse('CrudAssignment:retrieve'))
        self.assertEqual(response.status_code, 200)
