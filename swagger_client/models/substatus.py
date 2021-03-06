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


class Substatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, substatus=None, message=None):
        """
        Substatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'substatus': 'int',
            'message': 'str'
        }

        self.attribute_map = {
            'substatus': 'Substatus',
            'message': 'Message'
        }

        self._substatus = substatus
        self._message = message

    @property
    def substatus(self):
        """
        Gets the substatus of this Substatus.

        :return: The substatus of this Substatus.
        :rtype: int
        """
        return self._substatus

    @substatus.setter
    def substatus(self, substatus):
        """
        Sets the substatus of this Substatus.

        :param substatus: The substatus of this Substatus.
        :type: int
        """
        allowed_values = ["100", "101", "200", "201", "202", "203", "204", "205", "206", "300", "301", "302", "303", "304", "305", "306", "307", "400", "401", "402", "403", "404", "405", "406", "407", "408", "409", "410", "411", "412", "413", "414", "415", "416", "417", "426", "500", "501", "502", "503", "504", "505"]
        if substatus not in allowed_values:
            raise ValueError(
                "Invalid value for `substatus` ({0}), must be one of {1}"
                .format(substatus, allowed_values)
            )

        self._substatus = substatus

    @property
    def message(self):
        """
        Gets the message of this Substatus.

        :return: The message of this Substatus.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this Substatus.

        :param message: The message of this Substatus.
        :type: str
        """

        self._message = message

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
        if not isinstance(other, Substatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
