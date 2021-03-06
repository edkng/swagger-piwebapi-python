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
from swagger_client.apis.data_server_api import DataServerApi


class TestDataServerApi(unittest.TestCase):
    """ DataServerApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.data_server_api.DataServerApi()

    def tearDown(self):
        pass

    def test_data_server_create_enumeration_set(self):
        """
        Test case for data_server_create_enumeration_set

        Create an enumeration set on the Data Server.
        """
        pass

    def test_data_server_create_point(self):
        """
        Test case for data_server_create_point

        Create a point in the specified Data Server.
        """
        pass

    def test_data_server_get(self):
        """
        Test case for data_server_get

        Retrieve a Data Server.
        """
        pass

    def test_data_server_get_by_name(self):
        """
        Test case for data_server_get_by_name

        Retrieve a Data Server by name.
        """
        pass

    def test_data_server_get_by_path(self):
        """
        Test case for data_server_get_by_path

        Retrieve a Data Server by path.
        """
        pass

    def test_data_server_get_enumeration_sets(self):
        """
        Test case for data_server_get_enumeration_sets

        Retrieve enumeration sets for given Data Server.
        """
        pass

    def test_data_server_get_points(self):
        """
        Test case for data_server_get_points

        Retrieve a list of points on a specified Data Server.
        """
        pass

    def test_data_server_list(self):
        """
        Test case for data_server_list

        Retrieve a list of Data Servers known to this service.
        """
        pass


if __name__ == '__main__':
    unittest.main()
