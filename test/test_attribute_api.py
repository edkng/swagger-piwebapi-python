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
from swagger_client.apis.attribute_api import AttributeApi


class TestAttributeApi(unittest.TestCase):
    """ AttributeApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.attribute_api.AttributeApi()

    def tearDown(self):
        pass

    def test_attribute_create_attribute(self):
        """
        Test case for attribute_create_attribute

        Create a new attribute as a child of the specified attribute.
        """
        pass

    def test_attribute_create_config(self):
        """
        Test case for attribute_create_config

        Create or update an attribute's DataReference configuration (Create/Update PI point for PI Point DataReference).
        """
        pass

    def test_attribute_delete(self):
        """
        Test case for attribute_delete

        Delete an attribute.
        """
        pass

    def test_attribute_get(self):
        """
        Test case for attribute_get

        Retrieve an attribute.
        """
        pass

    def test_attribute_get_attributes(self):
        """
        Test case for attribute_get_attributes

        Get the child attributes of the specified attribute.
        """
        pass

    def test_attribute_get_by_path(self):
        """
        Test case for attribute_get_by_path

        Retrieve an attribute by path.
        """
        pass

    def test_attribute_get_categories(self):
        """
        Test case for attribute_get_categories

        Get an attribute's categories.
        """
        pass

    def test_attribute_get_multiple(self):
        """
        Test case for attribute_get_multiple

        Retrieve multiple attributes by web id or path.
        """
        pass

    def test_attribute_get_value(self):
        """
        Test case for attribute_get_value

        Get the attribute's value. This call is intended for use with attributes that have no data reference only. For attributes with a data reference, consult the documentation for Streams.
        """
        pass

    def test_attribute_set_value(self):
        """
        Test case for attribute_set_value

        Set the value of a configuration item attribute. For attributes with a data reference or non-configuration item attributes, consult the documentation for streams.
        """
        pass

    def test_attribute_update(self):
        """
        Test case for attribute_update

        Update an attribute by replacing items in its definition.
        """
        pass


if __name__ == '__main__':
    unittest.main()