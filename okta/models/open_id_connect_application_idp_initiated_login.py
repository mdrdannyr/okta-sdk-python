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

class OpenIdConnectApplicationIdpInitiatedLogin(object):
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
    swagger_types['mode'] = 'str'
    swagger_types['default_scope'] = 'list[str]'

    attribute_map = {
        'mode': 'mode',
        'default_scope': 'default_scope'
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

    def set_attributes(self, mode=None, default_scope=None, **kwargs):  # noqa: E501
        """OpenIdConnectApplicationIdpInitiatedLogin - a model defined in Swagger"""  # noqa: E501
        self._mode = None
        self._default_scope = None
        self.discriminator = None
        if mode is not None:
            if hasattr(models, self.swagger_types['mode']):
                nested_class = getattr(models, self.swagger_types['mode'])
                if isinstance(mode, nested_class):
                    self.mode = mode
                elif isinstance(mode, dict):
                    self.mode = nested_class.from_kwargs(**mode)
                else:
                    self.mode = mode
            else:
                self.mode = mode
        if default_scope is not None:
            if hasattr(models, self.swagger_types['default_scope']):
                nested_class = getattr(models, self.swagger_types['default_scope'])
                if isinstance(default_scope, nested_class):
                    self.default_scope = default_scope
                elif isinstance(default_scope, dict):
                    self.default_scope = nested_class.from_kwargs(**default_scope)
                else:
                    self.default_scope = default_scope
            else:
                self.default_scope = default_scope

    @property
    def mode(self):
        """Gets the mode of this OpenIdConnectApplicationIdpInitiatedLogin.  # noqa: E501


        :return: The mode of this OpenIdConnectApplicationIdpInitiatedLogin.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this OpenIdConnectApplicationIdpInitiatedLogin.


        :param mode: The mode of this OpenIdConnectApplicationIdpInitiatedLogin.  # noqa: E501
        :type: str
        """

        self._mode = mode

    @property
    def default_scope(self):
        """Gets the default_scope of this OpenIdConnectApplicationIdpInitiatedLogin.  # noqa: E501


        :return: The default_scope of this OpenIdConnectApplicationIdpInitiatedLogin.  # noqa: E501
        :rtype: list[str]
        """
        return self._default_scope

    @default_scope.setter
    def default_scope(self, default_scope):
        """Sets the default_scope of this OpenIdConnectApplicationIdpInitiatedLogin.


        :param default_scope: The default_scope of this OpenIdConnectApplicationIdpInitiatedLogin.  # noqa: E501
        :type: list[str]
        """

        self._default_scope = default_scope

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
        if issubclass(OpenIdConnectApplicationIdpInitiatedLogin, dict):
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
        if not isinstance(other, OpenIdConnectApplicationIdpInitiatedLogin):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
