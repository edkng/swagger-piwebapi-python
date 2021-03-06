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


class Attribute(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, web_id=None, id=None, name=None, description=None, path=None, type=None, type_qualifier=None, default_units_name=None, data_reference_plug_in=None, config_string=None, is_configuration_item=None, is_excluded=None, is_hidden=None, is_manual_data_entry=None, has_children=None, category_names=None, step=None, trait_name=None, links=None):
        """
        Attribute - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'web_id': 'str',
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'path': 'str',
            'type': 'str',
            'type_qualifier': 'str',
            'default_units_name': 'str',
            'data_reference_plug_in': 'str',
            'config_string': 'str',
            'is_configuration_item': 'bool',
            'is_excluded': 'bool',
            'is_hidden': 'bool',
            'is_manual_data_entry': 'bool',
            'has_children': 'bool',
            'category_names': 'list[str]',
            'step': 'bool',
            'trait_name': 'str',
            'links': 'InlineResponse20013Links'
        }

        self.attribute_map = {
            'web_id': 'WebId',
            'id': 'Id',
            'name': 'Name',
            'description': 'Description',
            'path': 'Path',
            'type': 'Type',
            'type_qualifier': 'TypeQualifier',
            'default_units_name': 'DefaultUnitsName',
            'data_reference_plug_in': 'DataReferencePlugIn',
            'config_string': 'ConfigString',
            'is_configuration_item': 'IsConfigurationItem',
            'is_excluded': 'IsExcluded',
            'is_hidden': 'IsHidden',
            'is_manual_data_entry': 'IsManualDataEntry',
            'has_children': 'HasChildren',
            'category_names': 'CategoryNames',
            'step': 'Step',
            'trait_name': 'TraitName',
            'links': 'Links'
        }

        self._web_id = web_id
        self._id = id
        self._name = name
        self._description = description
        self._path = path
        self._type = type
        self._type_qualifier = type_qualifier
        self._default_units_name = default_units_name
        self._data_reference_plug_in = data_reference_plug_in
        self._config_string = config_string
        self._is_configuration_item = is_configuration_item
        self._is_excluded = is_excluded
        self._is_hidden = is_hidden
        self._is_manual_data_entry = is_manual_data_entry
        self._has_children = has_children
        self._category_names = category_names
        self._step = step
        self._trait_name = trait_name
        self._links = links

    @property
    def web_id(self):
        """
        Gets the web_id of this Attribute.

        :return: The web_id of this Attribute.
        :rtype: str
        """
        return self._web_id

    @web_id.setter
    def web_id(self, web_id):
        """
        Sets the web_id of this Attribute.

        :param web_id: The web_id of this Attribute.
        :type: str
        """

        self._web_id = web_id

    @property
    def id(self):
        """
        Gets the id of this Attribute.

        :return: The id of this Attribute.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Attribute.

        :param id: The id of this Attribute.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Attribute.

        :return: The name of this Attribute.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Attribute.

        :param name: The name of this Attribute.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Attribute.

        :return: The description of this Attribute.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Attribute.

        :param description: The description of this Attribute.
        :type: str
        """

        self._description = description

    @property
    def path(self):
        """
        Gets the path of this Attribute.

        :return: The path of this Attribute.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this Attribute.

        :param path: The path of this Attribute.
        :type: str
        """

        self._path = path

    @property
    def type(self):
        """
        Gets the type of this Attribute.

        :return: The type of this Attribute.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Attribute.

        :param type: The type of this Attribute.
        :type: str
        """

        self._type = type

    @property
    def type_qualifier(self):
        """
        Gets the type_qualifier of this Attribute.

        :return: The type_qualifier of this Attribute.
        :rtype: str
        """
        return self._type_qualifier

    @type_qualifier.setter
    def type_qualifier(self, type_qualifier):
        """
        Sets the type_qualifier of this Attribute.

        :param type_qualifier: The type_qualifier of this Attribute.
        :type: str
        """

        self._type_qualifier = type_qualifier

    @property
    def default_units_name(self):
        """
        Gets the default_units_name of this Attribute.

        :return: The default_units_name of this Attribute.
        :rtype: str
        """
        return self._default_units_name

    @default_units_name.setter
    def default_units_name(self, default_units_name):
        """
        Sets the default_units_name of this Attribute.

        :param default_units_name: The default_units_name of this Attribute.
        :type: str
        """

        self._default_units_name = default_units_name

    @property
    def data_reference_plug_in(self):
        """
        Gets the data_reference_plug_in of this Attribute.

        :return: The data_reference_plug_in of this Attribute.
        :rtype: str
        """
        return self._data_reference_plug_in

    @data_reference_plug_in.setter
    def data_reference_plug_in(self, data_reference_plug_in):
        """
        Sets the data_reference_plug_in of this Attribute.

        :param data_reference_plug_in: The data_reference_plug_in of this Attribute.
        :type: str
        """

        self._data_reference_plug_in = data_reference_plug_in

    @property
    def config_string(self):
        """
        Gets the config_string of this Attribute.

        :return: The config_string of this Attribute.
        :rtype: str
        """
        return self._config_string

    @config_string.setter
    def config_string(self, config_string):
        """
        Sets the config_string of this Attribute.

        :param config_string: The config_string of this Attribute.
        :type: str
        """

        self._config_string = config_string

    @property
    def is_configuration_item(self):
        """
        Gets the is_configuration_item of this Attribute.

        :return: The is_configuration_item of this Attribute.
        :rtype: bool
        """
        return self._is_configuration_item

    @is_configuration_item.setter
    def is_configuration_item(self, is_configuration_item):
        """
        Sets the is_configuration_item of this Attribute.

        :param is_configuration_item: The is_configuration_item of this Attribute.
        :type: bool
        """

        self._is_configuration_item = is_configuration_item

    @property
    def is_excluded(self):
        """
        Gets the is_excluded of this Attribute.

        :return: The is_excluded of this Attribute.
        :rtype: bool
        """
        return self._is_excluded

    @is_excluded.setter
    def is_excluded(self, is_excluded):
        """
        Sets the is_excluded of this Attribute.

        :param is_excluded: The is_excluded of this Attribute.
        :type: bool
        """

        self._is_excluded = is_excluded

    @property
    def is_hidden(self):
        """
        Gets the is_hidden of this Attribute.

        :return: The is_hidden of this Attribute.
        :rtype: bool
        """
        return self._is_hidden

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """
        Sets the is_hidden of this Attribute.

        :param is_hidden: The is_hidden of this Attribute.
        :type: bool
        """

        self._is_hidden = is_hidden

    @property
    def is_manual_data_entry(self):
        """
        Gets the is_manual_data_entry of this Attribute.

        :return: The is_manual_data_entry of this Attribute.
        :rtype: bool
        """
        return self._is_manual_data_entry

    @is_manual_data_entry.setter
    def is_manual_data_entry(self, is_manual_data_entry):
        """
        Sets the is_manual_data_entry of this Attribute.

        :param is_manual_data_entry: The is_manual_data_entry of this Attribute.
        :type: bool
        """

        self._is_manual_data_entry = is_manual_data_entry

    @property
    def has_children(self):
        """
        Gets the has_children of this Attribute.

        :return: The has_children of this Attribute.
        :rtype: bool
        """
        return self._has_children

    @has_children.setter
    def has_children(self, has_children):
        """
        Sets the has_children of this Attribute.

        :param has_children: The has_children of this Attribute.
        :type: bool
        """

        self._has_children = has_children

    @property
    def category_names(self):
        """
        Gets the category_names of this Attribute.

        :return: The category_names of this Attribute.
        :rtype: list[str]
        """
        return self._category_names

    @category_names.setter
    def category_names(self, category_names):
        """
        Sets the category_names of this Attribute.

        :param category_names: The category_names of this Attribute.
        :type: list[str]
        """

        self._category_names = category_names

    @property
    def step(self):
        """
        Gets the step of this Attribute.

        :return: The step of this Attribute.
        :rtype: bool
        """
        return self._step

    @step.setter
    def step(self, step):
        """
        Sets the step of this Attribute.

        :param step: The step of this Attribute.
        :type: bool
        """

        self._step = step

    @property
    def trait_name(self):
        """
        Gets the trait_name of this Attribute.

        :return: The trait_name of this Attribute.
        :rtype: str
        """
        return self._trait_name

    @trait_name.setter
    def trait_name(self, trait_name):
        """
        Sets the trait_name of this Attribute.

        :param trait_name: The trait_name of this Attribute.
        :type: str
        """

        self._trait_name = trait_name

    @property
    def links(self):
        """
        Gets the links of this Attribute.

        :return: The links of this Attribute.
        :rtype: InlineResponse20013Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this Attribute.

        :param links: The links of this Attribute.
        :type: InlineResponse20013Links
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
        if not isinstance(other, Attribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
