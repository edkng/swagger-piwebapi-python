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
from swagger_client.apis.attribute_category_api import AttributeCategoryApi


class TestAttributeCategoryApi(unittest.TestCase):
    """ AttributeCategoryApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.attribute_category_api.AttributeCategoryApi()

    def tearDown(self):
        pass

    def test_attribute_category_create_security_entry(self):
        """
        Test case for attribute_category_create_security_entry

        Create a security entry owned by the attribute category.
        """
        pass

    def test_attribute_category_delete(self):
        """
        Test case for attribute_category_delete

        Delete an attribute category.
        """
        pass

    def test_attribute_category_delete_security_entry(self):
        """
        Test case for attribute_category_delete_security_entry

        Delete a security entry owned by the attribute category.
        """
        pass

    def test_attribute_category_get(self):
        """
        Test case for attribute_category_get

        Retrieve an attribute category.
        """
        pass

    def test_attribute_category_get_by_path(self):
        """
        Test case for attribute_category_get_by_path

        Retrieve an attribute category by path.
        """
        pass

    def test_attribute_category_get_security(self):
        """
        Test case for attribute_category_get_security

        Get the security information of the specified security item associated with the attribute category for a specified user.
        """
        pass

    def test_attribute_category_get_security_entries(self):
        """
        Test case for attribute_category_get_security_entries

        Retrieve the security entries associated with the attribute category based on the specified criteria. By default, all security entries for this attribute category are returned.
        """
        pass

    def test_attribute_category_get_security_entry_by_name(self):
        """
        Test case for attribute_category_get_security_entry_by_name

        Retrieve the security entry associated with the attribute category with the specified name.
        """
        pass

    def test_attribute_category_update(self):
        """
        Test case for attribute_category_update

        Update an attribute category by replacing items in its definition.
        """
        pass

    def test_attribute_category_update_security_entry(self):
        """
        Test case for attribute_category_update_security_entry

        Update a security entry owned by the attribute category.
        """
        pass


if __name__ == '__main__':
    unittest.main()
