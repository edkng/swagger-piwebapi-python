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


class PointAttribute(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, value=None, links=None):
        """
        PointAttribute - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'value': 'object',
            'links': 'InlineResponse20041Links'
        }

        self.attribute_map = {
            'name': 'Name',
            'value': 'Value',
            'links': 'Links'
        }

        self._name = name
        self._value = value
        self._links = links

    @property
    def name(self):
        """
        Gets the name of this PointAttribute.

        :return: The name of this PointAttribute.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PointAttribute.

        :param name: The name of this PointAttribute.
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """
        Gets the value of this PointAttribute.

        :return: The value of this PointAttribute.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this PointAttribute.

        :param value: The value of this PointAttribute.
        :type: object
        """

        self._value = value

    @property
    def links(self):
        """
        Gets the links of this PointAttribute.

        :return: The links of this PointAttribute.
        :rtype: InlineResponse20041Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this PointAttribute.

        :param links: The links of this PointAttribute.
        :type: InlineResponse20041Links
        """

        self._links = links

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
        if not isinstance(other, PointAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
