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
from swagger_client.apis.analysis_rule_api import AnalysisRuleApi


class TestAnalysisRuleApi(unittest.TestCase):
    """ AnalysisRuleApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.analysis_rule_api.AnalysisRuleApi()

    def tearDown(self):
        pass

    def test_analysis_rule_create_analysis_rule(self):
        """
        Test case for analysis_rule_create_analysis_rule

        Create a new Analysis Rule as a child of an existing Analysis Rule.
        """
        pass

    def test_analysis_rule_delete(self):
        """
        Test case for analysis_rule_delete

        Delete an Analysis Rule.
        """
        pass

    def test_analysis_rule_get(self):
        """
        Test case for analysis_rule_get

        Retrieve an Analysis Rule.
        """
        pass

    def test_analysis_rule_get_analysis_rules(self):
        """
        Test case for analysis_rule_get_analysis_rules

        Get the child Analysis Rules of the Analysis Rule.
        """
        pass

    def test_analysis_rule_get_by_path(self):
        """
        Test case for analysis_rule_get_by_path

        Retrieve an Analysis Rule by path.
        """
        pass

    def test_analysis_rule_update(self):
        """
        Test case for analysis_rule_update

        Update an Analysis Rule by replacing items in its definition.
        """
        pass


if __name__ == '__main__':
    unittest.main()
