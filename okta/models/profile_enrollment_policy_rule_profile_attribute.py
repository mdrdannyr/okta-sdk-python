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

class ProfileEnrollmentPolicyRuleProfileAttribute(object):
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
    swagger_types['label'] = 'str'
    swagger_types['name'] = 'str'
    swagger_types['required'] = 'bool'

    attribute_map = {
        'label': 'label',
        'name': 'name',
        'required': 'required'
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

    def set_attributes(self, label=None, name=None, required=None, **kwargs):  # noqa: E501
        """ProfileEnrollmentPolicyRuleProfileAttribute - a model defined in Swagger"""  # noqa: E501
        self._label = None
        self._name = None
        self._required = None
        self.discriminator = None
        if label is not None:
            if hasattr(models, self.swagger_types['label']):
                nested_class = getattr(models, self.swagger_types['label'])
                if isinstance(label, nested_class):
                    self.label = label
                elif isinstance(label, dict):
                    self.label = nested_class.from_kwargs(**label)
                else:
                    self.label = label
            else:
                self.label = label
        if name is not None:
            if hasattr(models, self.swagger_types['name']):
                nested_class = getattr(models, self.swagger_types['name'])
                if isinstance(name, nested_class):
                    self.name = name
                elif isinstance(name, dict):
                    self.name = nested_class.from_kwargs(**name)
                else:
                    self.name = name
            else:
                self.name = name
        if required is not None:
            if hasattr(models, self.swagger_types['required']):
                nested_class = getattr(models, self.swagger_types['required'])
                if isinstance(required, nested_class):
                    self.required = required
                elif isinstance(required, dict):
                    self.required = nested_class.from_kwargs(**required)
                else:
                    self.required = required
            else:
                self.required = required

    @property
    def label(self):
        """Gets the label of this ProfileEnrollmentPolicyRuleProfileAttribute.  # noqa: E501


        :return: The label of this ProfileEnrollmentPolicyRuleProfileAttribute.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ProfileEnrollmentPolicyRuleProfileAttribute.


        :param label: The label of this ProfileEnrollmentPolicyRuleProfileAttribute.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def name(self):
        """Gets the name of this ProfileEnrollmentPolicyRuleProfileAttribute.  # noqa: E501


        :return: The name of this ProfileEnrollmentPolicyRuleProfileAttribute.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProfileEnrollmentPolicyRuleProfileAttribute.


        :param name: The name of this ProfileEnrollmentPolicyRuleProfileAttribute.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def required(self):
        """Gets the required of this ProfileEnrollmentPolicyRuleProfileAttribute.  # noqa: E501


        :return: The required of this ProfileEnrollmentPolicyRuleProfileAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this ProfileEnrollmentPolicyRuleProfileAttribute.


        :param required: The required of this ProfileEnrollmentPolicyRuleProfileAttribute.  # noqa: E501
        :type: bool
        """

        self._required = required

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
        if issubclass(ProfileEnrollmentPolicyRuleProfileAttribute, dict):
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
        if not isinstance(other, ProfileEnrollmentPolicyRuleProfileAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
