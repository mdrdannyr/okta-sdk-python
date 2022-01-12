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

class CreateUserRequest(object):
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
    swagger_types['credentials'] = 'UserCredentials'
    swagger_types['group_ids'] = 'list[str]'
    swagger_types['profile'] = 'UserProfile'
    swagger_types['type'] = 'UserType'

    attribute_map = {
        'credentials': 'credentials',
        'group_ids': 'groupIds',
        'profile': 'profile',
        'type': 'type'
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

    def set_attributes(self, credentials=None, group_ids=None, profile=None, type=None, **kwargs):  # noqa: E501
        """CreateUserRequest - a model defined in Swagger"""  # noqa: E501
        self._credentials = None
        self._group_ids = None
        self._profile = None
        self._type = None
        self.discriminator = None
        if credentials is not None:
            if hasattr(models, self.swagger_types['credentials']):
                nested_class = getattr(models, self.swagger_types['credentials'])
                if isinstance(credentials, nested_class):
                    self.credentials = credentials
                elif isinstance(credentials, dict):
                    self.credentials = nested_class.from_kwargs(**credentials)
                else:
                    self.credentials = credentials
            else:
                self.credentials = credentials
        if group_ids is not None:
            if hasattr(models, self.swagger_types['group_ids']):
                nested_class = getattr(models, self.swagger_types['group_ids'])
                if isinstance(group_ids, nested_class):
                    self.group_ids = group_ids
                elif isinstance(group_ids, dict):
                    self.group_ids = nested_class.from_kwargs(**group_ids)
                else:
                    self.group_ids = group_ids
            else:
                self.group_ids = group_ids
        if profile is not None:
            if hasattr(models, self.swagger_types['profile']):
                nested_class = getattr(models, self.swagger_types['profile'])
                if isinstance(profile, nested_class):
                    self.profile = profile
                elif isinstance(profile, dict):
                    self.profile = nested_class.from_kwargs(**profile)
                else:
                    self.profile = profile
            else:
                self.profile = profile
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

    @property
    def credentials(self):
        """Gets the credentials of this CreateUserRequest.  # noqa: E501


        :return: The credentials of this CreateUserRequest.  # noqa: E501
        :rtype: UserCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this CreateUserRequest.


        :param credentials: The credentials of this CreateUserRequest.  # noqa: E501
        :type: UserCredentials
        """

        self._credentials = credentials

    @property
    def group_ids(self):
        """Gets the group_ids of this CreateUserRequest.  # noqa: E501


        :return: The group_ids of this CreateUserRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        """Sets the group_ids of this CreateUserRequest.


        :param group_ids: The group_ids of this CreateUserRequest.  # noqa: E501
        :type: list[str]
        """

        self._group_ids = group_ids

    @property
    def profile(self):
        """Gets the profile of this CreateUserRequest.  # noqa: E501


        :return: The profile of this CreateUserRequest.  # noqa: E501
        :rtype: UserProfile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this CreateUserRequest.


        :param profile: The profile of this CreateUserRequest.  # noqa: E501
        :type: UserProfile
        """

        self._profile = profile

    @property
    def type(self):
        """Gets the type of this CreateUserRequest.  # noqa: E501


        :return: The type of this CreateUserRequest.  # noqa: E501
        :rtype: UserType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateUserRequest.


        :param type: The type of this CreateUserRequest.  # noqa: E501
        :type: UserType
        """

        self._type = type

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
        if issubclass(CreateUserRequest, dict):
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
        if not isinstance(other, CreateUserRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
