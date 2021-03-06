# coding: utf-8

"""
    PI Web API 2017 Swagger Spec

    Swagger Spec file that describes PI Web API

    OpenAPI spec version: 1.9.0.266
    Contact: techsupport@osisoft.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TableData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, columns=None, rows=None):
        """
        TableData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'columns': 'dict(str, str)',
            'rows': 'list[dict(str, object)]'
        }

        self.attribute_map = {
            'columns': 'Columns',
            'rows': 'Rows'
        }

        self._columns = columns
        self._rows = rows

    @property
    def columns(self):
        """
        Gets the columns of this TableData.

        :return: The columns of this TableData.
        :rtype: dict(str, str)
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """
        Sets the columns of this TableData.

        :param columns: The columns of this TableData.
        :type: dict(str, str)
        """

        self._columns = columns

    @property
    def rows(self):
        """
        Gets the rows of this TableData.

        :return: The rows of this TableData.
        :rtype: list[dict(str, object)]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """
        Sets the rows of this TableData.

        :param rows: The rows of this TableData.
        :type: list[dict(str, object)]
        """

        self._rows = rows

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, TableData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
