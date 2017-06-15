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
from swagger_client.apis.table_api import TableApi


class TestTableApi(unittest.TestCase):
    """ TableApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.table_api.TableApi()

    def tearDown(self):
        pass

    def test_table_create_security_entry(self):
        """
        Test case for table_create_security_entry

        Create a security entry owned by the table.
        """
        pass

    def test_table_delete(self):
        """
        Test case for table_delete

        Delete a table.
        """
        pass

    def test_table_delete_security_entry(self):
        """
        Test case for table_delete_security_entry

        Delete a security entry owned by the table.
        """
        pass

    def test_table_get(self):
        """
        Test case for table_get

        Retrieve a table.
        """
        pass

    def test_table_get_by_path(self):
        """
        Test case for table_get_by_path

        Retrieve a table by path.
        """
        pass

    def test_table_get_categories(self):
        """
        Test case for table_get_categories

        Get a table's categories.
        """
        pass

    def test_table_get_data(self):
        """
        Test case for table_get_data

        Get the table's data.
        """
        pass

    def test_table_get_security(self):
        """
        Test case for table_get_security

        Get the security information of the specified security item associated with the table for a specified user.
        """
        pass

    def test_table_get_security_entries(self):
        """
        Test case for table_get_security_entries

        Retrieve the security entries associated with the table based on the specified criteria. By default, all security entries for this table are returned.
        """
        pass

    def test_table_get_security_entry_by_name(self):
        """
        Test case for table_get_security_entry_by_name

        Retrieve the security entry associated with the table with the specified name.
        """
        pass

    def test_table_update(self):
        """
        Test case for table_update

        Update a table by replacing items in its definition.
        """
        pass

    def test_table_update_data(self):
        """
        Test case for table_update_data

        Update the table's data.
        """
        pass

    def test_table_update_security_entry(self):
        """
        Test case for table_update_security_entry

        Update a security entry owned by the table.
        """
        pass


if __name__ == '__main__':
    unittest.main()