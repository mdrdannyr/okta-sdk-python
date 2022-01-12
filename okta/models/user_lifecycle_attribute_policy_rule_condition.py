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

class UserLifecycleAttributePolicyRuleCondition(object):
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
    swagger_types['attribute_name'] = 'str'
    swagger_types['matching_value'] = 'str'

    attribute_map = {
        'attribute_name': 'attributeName',
        'matching_value': 'matchingValue'
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

    def set_attributes(self, attribute_name=None, matching_value=None, **kwargs):  # noqa: E501
        """UserLifecycleAttributePolicyRuleCondition - a model defined in Swagger"""  # noqa: E501
        self._attribute_name = None
        self._matching_value = None
        self.discriminator = None
        if attribute_name is not None:
            if hasattr(models, self.swagger_types['attribute_name']):
                nested_class = getattr(models, self.swagger_types['attribute_name'])
                if isinstance(attribute_name, nested_class):
                    self.attribute_name = attribute_name
                elif isinstance(attribute_name, dict):
                    self.attribute_name = nested_class.from_kwargs(**attribute_name)
                else:
                    self.attribute_name = attribute_name
            else:
                self.attribute_name = attribute_name
        if matching_value is not None:
            if hasattr(models, self.swagger_types['matching_value']):
                nested_class = getattr(models, self.swagger_types['matching_value'])
                if isinstance(matching_value, nested_class):
                    self.matching_value = matching_value
                elif isinstance(matching_value, dict):
                    self.matching_value = nested_class.from_kwargs(**matching_value)
                else:
                    self.matching_value = matching_value
            else:
                self.matching_value = matching_value

    @property
    def attribute_name(self):
        """Gets the attribute_name of this UserLifecycleAttributePolicyRuleCondition.  # noqa: E501


        :return: The attribute_name of this UserLifecycleAttributePolicyRuleCondition.  # noqa: E501
        :rtype: str
        """
        return self._attribute_name

    @attribute_name.setter
    def attribute_name(self, attribute_name):
        """Sets the attribute_name of this UserLifecycleAttributePolicyRuleCondition.


        :param attribute_name: The attribute_name of this UserLifecycleAttributePolicyRuleCondition.  # noqa: E501
        :type: str
        """

        self._attribute_name = attribute_name

    @property
    def matching_value(self):
        """Gets the matching_value of this UserLifecycleAttributePolicyRuleCondition.  # noqa: E501


        :return: The matching_value of this UserLifecycleAttributePolicyRuleCondition.  # noqa: E501
        :rtype: str
        """
        return self._matching_value

    @matching_value.setter
    def matching_value(self, matching_value):
        """Sets the matching_value of this UserLifecycleAttributePolicyRuleCondition.


        :param matching_value: The matching_value of this UserLifecycleAttributePolicyRuleCondition.  # noqa: E501
        :type: str
        """

        self._matching_value = matching_value

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
        if issubclass(UserLifecycleAttributePolicyRuleCondition, dict):
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
        if not isinstance(other, UserLifecycleAttributePolicyRuleCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
