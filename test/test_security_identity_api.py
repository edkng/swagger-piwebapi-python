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
from swagger_client.apis.security_identity_api import SecurityIdentityApi


class TestSecurityIdentityApi(unittest.TestCase):
    """ SecurityIdentityApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.security_identity_api.SecurityIdentityApi()

    def tearDown(self):
        pass

    def test_security_identity_delete(self):
        """
        Test case for security_identity_delete

        Delete a security identity.
        """
        pass

    def test_security_identity_get(self):
        """
        Test case for security_identity_get

        Retrieve a security identity.
        """
        pass

    def test_security_identity_get_by_path(self):
        """
        Test case for security_identity_get_by_path

        Retrieve a security identity by path.
        """
        pass

    def test_security_identity_get_security(self):
        """
        Test case for security_identity_get_security

        Get the security information of the specified security item associated with the security identity for a specified user.
        """
        pass

    def test_security_identity_get_security_entries(self):
        """
        Test case for security_identity_get_security_entries

        Retrieve the security entries associated with the security identity based on the specified criteria. By default, all security entries for this security identity are returned.
        """
        pass

    def test_security_identity_get_security_entry_by_name(self):
        """
        Test case for security_identity_get_security_entry_by_name

        Retrieve the security entry associated with the security identity with the specified name.
        """
        pass

    def test_security_identity_get_security_mappings(self):
        """
        Test case for security_identity_get_security_mappings

        Get security mappings for the specified security identity.
        """
        pass

    def test_security_identity_update(self):
        """
        Test case for security_identity_update

        Update a security identity by replacing items in its definition.
        """
        pass


if __name__ == '__main__':
    unittest.main()
