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

class CsrMetadataSubjectAltNames(object):
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
    swagger_types['dns_names'] = 'list[str]'

    attribute_map = {
        'dns_names': 'dnsNames'
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

    def set_attributes(self, dns_names=None, **kwargs):  # noqa: E501
        """CsrMetadataSubjectAltNames - a model defined in Swagger"""  # noqa: E501
        self._dns_names = None
        self.discriminator = None
        if dns_names is not None:
            if hasattr(models, self.swagger_types['dns_names']):
                nested_class = getattr(models, self.swagger_types['dns_names'])
                if isinstance(dns_names, nested_class):
                    self.dns_names = dns_names
                elif isinstance(dns_names, dict):
                    self.dns_names = nested_class.from_kwargs(**dns_names)
                else:
                    self.dns_names = dns_names
            else:
                self.dns_names = dns_names

    @property
    def dns_names(self):
        """Gets the dns_names of this CsrMetadataSubjectAltNames.  # noqa: E501


        :return: The dns_names of this CsrMetadataSubjectAltNames.  # noqa: E501
        :rtype: list[str]
        """
        return self._dns_names

    @dns_names.setter
    def dns_names(self, dns_names):
        """Sets the dns_names of this CsrMetadataSubjectAltNames.


        :param dns_names: The dns_names of this CsrMetadataSubjectAltNames.  # noqa: E501
        :type: list[str]
        """

        self._dns_names = dns_names

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
        if issubclass(CsrMetadataSubjectAltNames, dict):
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
        if not isinstance(other, CsrMetadataSubjectAltNames):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
