# coding: utf-8

"""
    PI Web API 2017 Swagger Spec

    Swagger Spec file that describes PI Web API

    OpenAPI spec version: 1.9.0.266
    Contact: techsupport@osisoft.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.enumeration_value_api import EnumerationValueApi


class TestEnumerationValueApi(unittest.TestCase):
    """ EnumerationValueApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.enumeration_value_api.EnumerationValueApi()

    def tearDown(self):
        pass

    def test_enumeration_value_delete_enumeration_value(self):
        """
        Test case for enumeration_value_delete_enumeration_value

        Delete an enumeration value from an enumeration set.
        """
        pass

    def test_enumeration_value_get(self):
        """
        Test case for enumeration_value_get

        Retrieve an enumeration value mapping
        """
        pass

    def test_enumeration_value_get_by_path(self):
        """
        Test case for enumeration_value_get_by_path

        Retrieve an enumeration value by path.
        """
        pass

    def test_enumeration_value_update_enumeration_value(self):
        """
        Test case for enumeration_value_update_enumeration_value

        Update an enumeration value by replacing items in its definition.
        """
        pass


if __name__ == '__main__':
    unittest.main()