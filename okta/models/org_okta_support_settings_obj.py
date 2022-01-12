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

class OrgOktaSupportSettingsObj(object):
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
    swagger_types['links'] = 'dict(str, object)'
    swagger_types['expiration'] = 'datetime'
    swagger_types['support'] = 'OrgOktaSupportSetting'

    attribute_map = {
        'links': '_links',
        'expiration': 'expiration',
        'support': 'support'
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

    def set_attributes(self, links=None, expiration=None, support=None, **kwargs):  # noqa: E501
        """OrgOktaSupportSettingsObj - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self._expiration = None
        self._support = None
        self.discriminator = None
        if links is not None:
            if hasattr(models, self.swagger_types['links']):
                nested_class = getattr(models, self.swagger_types['links'])
                if isinstance(links, nested_class):
                    self.links = links
                elif isinstance(links, dict):
                    self.links = nested_class.from_kwargs(**links)
                else:
                    self.links = links
            else:
                self.links = links
        if expiration is not None:
            if hasattr(models, self.swagger_types['expiration']):
                nested_class = getattr(models, self.swagger_types['expiration'])
                if isinstance(expiration, nested_class):
                    self.expiration = expiration
                elif isinstance(expiration, dict):
                    self.expiration = nested_class.from_kwargs(**expiration)
                else:
                    self.expiration = expiration
            else:
                self.expiration = expiration
        if support is not None:
            if hasattr(models, self.swagger_types['support']):
                nested_class = getattr(models, self.swagger_types['support'])
                if isinstance(support, nested_class):
                    self.support = support
                elif isinstance(support, dict):
                    self.support = nested_class.from_kwargs(**support)
                else:
                    self.support = support
            else:
                self.support = support

    @property
    def links(self):
        """Gets the links of this OrgOktaSupportSettingsObj.  # noqa: E501


        :return: The links of this OrgOktaSupportSettingsObj.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this OrgOktaSupportSettingsObj.


        :param links: The links of this OrgOktaSupportSettingsObj.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

    @property
    def expiration(self):
        """Gets the expiration of this OrgOktaSupportSettingsObj.  # noqa: E501


        :return: The expiration of this OrgOktaSupportSettingsObj.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this OrgOktaSupportSettingsObj.


        :param expiration: The expiration of this OrgOktaSupportSettingsObj.  # noqa: E501
        :type: datetime
        """

        self._expiration = expiration

    @property
    def support(self):
        """Gets the support of this OrgOktaSupportSettingsObj.  # noqa: E501


        :return: The support of this OrgOktaSupportSettingsObj.  # noqa: E501
        :rtype: OrgOktaSupportSetting
        """
        return self._support

    @support.setter
    def support(self, support):
        """Sets the support of this OrgOktaSupportSettingsObj.


        :param support: The support of this OrgOktaSupportSettingsObj.  # noqa: E501
        :type: OrgOktaSupportSetting
        """

        self._support = support

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
        if issubclass(OrgOktaSupportSettingsObj, dict):
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
        if not isinstance(other, OrgOktaSupportSettingsObj):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
