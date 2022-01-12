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

class CAPTCHAInstance(object):
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
    swagger_types['id'] = 'str'
    swagger_types['name'] = 'str'
    swagger_types['secret_key'] = 'str'
    swagger_types['site_key'] = 'str'
    swagger_types['type'] = 'CAPTCHAType'
    swagger_types['link'] = 'CAPTCHAInstanceLink'

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'secret_key': 'secretKey',
        'site_key': 'siteKey',
        'type': 'type',
        'link': '_link'
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

    def set_attributes(self, id=None, name=None, secret_key=None, site_key=None, type=None, link=None, **kwargs):  # noqa: E501
        """CAPTCHAInstance - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._secret_key = None
        self._site_key = None
        self._type = None
        self._link = None
        self.discriminator = None
        if id is not None:
            if hasattr(models, self.swagger_types['id']):
                nested_class = getattr(models, self.swagger_types['id'])
                if isinstance(id, nested_class):
                    self.id = id
                elif isinstance(id, dict):
                    self.id = nested_class.from_kwargs(**id)
                else:
                    self.id = id
            else:
                self.id = id
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
        if secret_key is not None:
            if hasattr(models, self.swagger_types['secret_key']):
                nested_class = getattr(models, self.swagger_types['secret_key'])
                if isinstance(secret_key, nested_class):
                    self.secret_key = secret_key
                elif isinstance(secret_key, dict):
                    self.secret_key = nested_class.from_kwargs(**secret_key)
                else:
                    self.secret_key = secret_key
            else:
                self.secret_key = secret_key
        if site_key is not None:
            if hasattr(models, self.swagger_types['site_key']):
                nested_class = getattr(models, self.swagger_types['site_key'])
                if isinstance(site_key, nested_class):
                    self.site_key = site_key
                elif isinstance(site_key, dict):
                    self.site_key = nested_class.from_kwargs(**site_key)
                else:
                    self.site_key = site_key
            else:
                self.site_key = site_key
        if type is not None:
            if hasattr(models, self.swagger_types['type']):
                nested_class = getattr(models, self.swagger_types['type'])
                if isinstance(type, nested_class):
                    self.type = type
                elif isinstance(type, dict):
                    self.type = nested_class.from_kwargs(**type)
                else:
                    self.type = type
            else:
                self.type = type
        if link is not None:
            if hasattr(models, self.swagger_types['link']):
                nested_class = getattr(models, self.swagger_types['link'])
                if isinstance(link, nested_class):
                    self.link = link
                elif isinstance(link, dict):
                    self.link = nested_class.from_kwargs(**link)
                else:
                    self.link = link
            else:
                self.link = link

    @property
    def id(self):
        """Gets the id of this CAPTCHAInstance.  # noqa: E501


        :return: The id of this CAPTCHAInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CAPTCHAInstance.


        :param id: The id of this CAPTCHAInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this CAPTCHAInstance.  # noqa: E501


        :return: The name of this CAPTCHAInstance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CAPTCHAInstance.


        :param name: The name of this CAPTCHAInstance.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def secret_key(self):
        """Gets the secret_key of this CAPTCHAInstance.  # noqa: E501


        :return: The secret_key of this CAPTCHAInstance.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this CAPTCHAInstance.


        :param secret_key: The secret_key of this CAPTCHAInstance.  # noqa: E501
        :type: str
        """

        self._secret_key = secret_key

    @property
    def site_key(self):
        """Gets the site_key of this CAPTCHAInstance.  # noqa: E501


        :return: The site_key of this CAPTCHAInstance.  # noqa: E501
        :rtype: str
        """
        return self._site_key

    @site_key.setter
    def site_key(self, site_key):
        """Sets the site_key of this CAPTCHAInstance.


        :param site_key: The site_key of this CAPTCHAInstance.  # noqa: E501
        :type: str
        """

        self._site_key = site_key

    @property
    def type(self):
        """Gets the type of this CAPTCHAInstance.  # noqa: E501


        :return: The type of this CAPTCHAInstance.  # noqa: E501
        :rtype: CAPTCHAType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CAPTCHAInstance.


        :param type: The type of this CAPTCHAInstance.  # noqa: E501
        :type: CAPTCHAType
        """

        self._type = type

    @property
    def link(self):
        """Gets the link of this CAPTCHAInstance.  # noqa: E501


        :return: The link of this CAPTCHAInstance.  # noqa: E501
        :rtype: CAPTCHAInstanceLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this CAPTCHAInstance.


        :param link: The link of this CAPTCHAInstance.  # noqa: E501
        :type: CAPTCHAInstanceLink
        """

        self._link = link

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
        if issubclass(CAPTCHAInstance, dict):
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
        if not isinstance(other, CAPTCHAInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
