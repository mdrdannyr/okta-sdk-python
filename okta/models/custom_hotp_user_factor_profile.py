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

class CustomHotpUserFactorProfile(object):
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
    swagger_types['shared_secret'] = 'str'

    attribute_map = {
        'shared_secret': 'sharedSecret'
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

    def set_attributes(self, shared_secret=None, **kwargs):  # noqa: E501
        """CustomHotpUserFactorProfile - a model defined in Swagger"""  # noqa: E501
        self._shared_secret = None
        self.discriminator = None
        if shared_secret is not None:
            if hasattr(models, self.swagger_types['shared_secret']):
                nested_class = getattr(models, self.swagger_types['shared_secret'])
                if isinstance(shared_secret, nested_class):
                    self.shared_secret = shared_secret
                elif isinstance(shared_secret, dict):
                    self.shared_secret = nested_class.from_kwargs(**shared_secret)
                else:
                    self.shared_secret = shared_secret
            else:
                self.shared_secret = shared_secret

    @property
    def shared_secret(self):
        """Gets the shared_secret of this CustomHotpUserFactorProfile.  # noqa: E501


        :return: The shared_secret of this CustomHotpUserFactorProfile.  # noqa: E501
        :rtype: str
        """
        return self._shared_secret

    @shared_secret.setter
    def shared_secret(self, shared_secret):
        """Sets the shared_secret of this CustomHotpUserFactorProfile.


        :param shared_secret: The shared_secret of this CustomHotpUserFactorProfile.  # noqa: E501
        :type: str
        """

        self._shared_secret = shared_secret

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
        if issubclass(CustomHotpUserFactorProfile, dict):
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
        if not isinstance(other, CustomHotpUserFactorProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
