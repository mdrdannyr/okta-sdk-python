# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API  # noqa: E501

    OpenAPI spec version: 2.9.2
    Contact: devex-public@okta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

import okta.models as models  # noqa
from okta.helpers import to_snake_case

class Duration(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    swagger_types['number'] = 'int'
    swagger_types['unit'] = 'str'

    attribute_map = {
        'number': 'number',
        'unit': 'unit'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
        else:
            config = {}
        self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, number=None, unit=None, **kwargs):  # noqa: E501
        """Duration - a model defined in Swagger"""  # noqa: E501
        self._number = None
        self._unit = None
        self.discriminator = None
        if number is not None:
            if hasattr(models, self.swagger_types['number']):
                nested_class = getattr(models, self.swagger_types['number'])
                if isinstance(number, nested_class):
                    self.number = number
                elif isinstance(number, dict):
                    self.number = nested_class.from_kwargs(**number)
                else:
                    self.number = number
            else:
                self.number = number
        if unit is not None:
            if hasattr(models, self.swagger_types['unit']):
                nested_class = getattr(models, self.swagger_types['unit'])
                if isinstance(unit, nested_class):
                    self.unit = unit
                elif isinstance(unit, dict):
                    self.unit = nested_class.from_kwargs(**unit)
                else:
                    self.unit = unit
            else:
                self.unit = unit

    @property
    def number(self):
        """Gets the number of this Duration.  # noqa: E501


        :return: The number of this Duration.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Duration.


        :param number: The number of this Duration.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def unit(self):
        """Gets the unit of this Duration.  # noqa: E501


        :return: The unit of this Duration.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Duration.


        :param unit: The unit of this Duration.  # noqa: E501
        :type: str
        """

        self._unit = unit

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Duration, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Duration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
