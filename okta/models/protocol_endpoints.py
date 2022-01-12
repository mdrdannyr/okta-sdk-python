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

class ProtocolEndpoints(object):
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
    swagger_types['acs'] = 'ProtocolEndpoint'
    swagger_types['authorization'] = 'ProtocolEndpoint'
    swagger_types['jwks'] = 'ProtocolEndpoint'
    swagger_types['metadata'] = 'ProtocolEndpoint'
    swagger_types['slo'] = 'ProtocolEndpoint'
    swagger_types['sso'] = 'ProtocolEndpoint'
    swagger_types['token'] = 'ProtocolEndpoint'
    swagger_types['user_info'] = 'ProtocolEndpoint'

    attribute_map = {
        'acs': 'acs',
        'authorization': 'authorization',
        'jwks': 'jwks',
        'metadata': 'metadata',
        'slo': 'slo',
        'sso': 'sso',
        'token': 'token',
        'user_info': 'userInfo'
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

    def set_attributes(self, acs=None, authorization=None, jwks=None, metadata=None, slo=None, sso=None, token=None, user_info=None, **kwargs):  # noqa: E501
        """ProtocolEndpoints - a model defined in Swagger"""  # noqa: E501
        self._acs = None
        self._authorization = None
        self._jwks = None
        self._metadata = None
        self._slo = None
        self._sso = None
        self._token = None
        self._user_info = None
        self.discriminator = None
        if acs is not None:
            if hasattr(models, self.swagger_types['acs']):
                nested_class = getattr(models, self.swagger_types['acs'])
                if isinstance(acs, nested_class):
                    self.acs = acs
                elif isinstance(acs, dict):
                    self.acs = nested_class.from_kwargs(**acs)
                else:
                    self.acs = acs
            else:
                self.acs = acs
        if authorization is not None:
            if hasattr(models, self.swagger_types['authorization']):
                nested_class = getattr(models, self.swagger_types['authorization'])
                if isinstance(authorization, nested_class):
                    self.authorization = authorization
                elif isinstance(authorization, dict):
                    self.authorization = nested_class.from_kwargs(**authorization)
                else:
                    self.authorization = authorization
            else:
                self.authorization = authorization
        if jwks is not None:
            if hasattr(models, self.swagger_types['jwks']):
                nested_class = getattr(models, self.swagger_types['jwks'])
                if isinstance(jwks, nested_class):
                    self.jwks = jwks
                elif isinstance(jwks, dict):
                    self.jwks = nested_class.from_kwargs(**jwks)
                else:
                    self.jwks = jwks
            else:
                self.jwks = jwks
        if metadata is not None:
            if hasattr(models, self.swagger_types['metadata']):
                nested_class = getattr(models, self.swagger_types['metadata'])
                if isinstance(metadata, nested_class):
                    self.metadata = metadata
                elif isinstance(metadata, dict):
                    self.metadata = nested_class.from_kwargs(**metadata)
                else:
                    self.metadata = metadata
            else:
                self.metadata = metadata
        if slo is not None:
            if hasattr(models, self.swagger_types['slo']):
                nested_class = getattr(models, self.swagger_types['slo'])
                if isinstance(slo, nested_class):
                    self.slo = slo
                elif isinstance(slo, dict):
                    self.slo = nested_class.from_kwargs(**slo)
                else:
                    self.slo = slo
            else:
                self.slo = slo
        if sso is not None:
            if hasattr(models, self.swagger_types['sso']):
                nested_class = getattr(models, self.swagger_types['sso'])
                if isinstance(sso, nested_class):
                    self.sso = sso
                elif isinstance(sso, dict):
                    self.sso = nested_class.from_kwargs(**sso)
                else:
                    self.sso = sso
            else:
                self.sso = sso
        if token is not None:
            if hasattr(models, self.swagger_types['token']):
                nested_class = getattr(models, self.swagger_types['token'])
                if isinstance(token, nested_class):
                    self.token = token
                elif isinstance(token, dict):
                    self.token = nested_class.from_kwargs(**token)
                else:
                    self.token = token
            else:
                self.token = token
        if user_info is not None:
            if hasattr(models, self.swagger_types['user_info']):
                nested_class = getattr(models, self.swagger_types['user_info'])
                if isinstance(user_info, nested_class):
                    self.user_info = user_info
                elif isinstance(user_info, dict):
                    self.user_info = nested_class.from_kwargs(**user_info)
                else:
                    self.user_info = user_info
            else:
                self.user_info = user_info

    @property
    def acs(self):
        """Gets the acs of this ProtocolEndpoints.  # noqa: E501


        :return: The acs of this ProtocolEndpoints.  # noqa: E501
        :rtype: ProtocolEndpoint
        """
        return self._acs

    @acs.setter
    def acs(self, acs):
        """Sets the acs of this ProtocolEndpoints.


        :param acs: The acs of this ProtocolEndpoints.  # noqa: E501
        :type: ProtocolEndpoint
        """

        self._acs = acs

    @property
    def authorization(self):
        """Gets the authorization of this ProtocolEndpoints.  # noqa: E501


        :return: The authorization of this ProtocolEndpoints.  # noqa: E501
        :rtype: ProtocolEndpoint
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this ProtocolEndpoints.


        :param authorization: The authorization of this ProtocolEndpoints.  # noqa: E501
        :type: ProtocolEndpoint
        """

        self._authorization = authorization

    @property
    def jwks(self):
        """Gets the jwks of this ProtocolEndpoints.  # noqa: E501


        :return: The jwks of this ProtocolEndpoints.  # noqa: E501
        :rtype: ProtocolEndpoint
        """
        return self._jwks

    @jwks.setter
    def jwks(self, jwks):
        """Sets the jwks of this ProtocolEndpoints.


        :param jwks: The jwks of this ProtocolEndpoints.  # noqa: E501
        :type: ProtocolEndpoint
        """

        self._jwks = jwks

    @property
    def metadata(self):
        """Gets the metadata of this ProtocolEndpoints.  # noqa: E501


        :return: The metadata of this ProtocolEndpoints.  # noqa: E501
        :rtype: ProtocolEndpoint
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ProtocolEndpoints.


        :param metadata: The metadata of this ProtocolEndpoints.  # noqa: E501
        :type: ProtocolEndpoint
        """

        self._metadata = metadata

    @property
    def slo(self):
        """Gets the slo of this ProtocolEndpoints.  # noqa: E501


        :return: The slo of this ProtocolEndpoints.  # noqa: E501
        :rtype: ProtocolEndpoint
        """
        return self._slo

    @slo.setter
    def slo(self, slo):
        """Sets the slo of this ProtocolEndpoints.


        :param slo: The slo of this ProtocolEndpoints.  # noqa: E501
        :type: ProtocolEndpoint
        """

        self._slo = slo

    @property
    def sso(self):
        """Gets the sso of this ProtocolEndpoints.  # noqa: E501


        :return: The sso of this ProtocolEndpoints.  # noqa: E501
        :rtype: ProtocolEndpoint
        """
        return self._sso

    @sso.setter
    def sso(self, sso):
        """Sets the sso of this ProtocolEndpoints.


        :param sso: The sso of this ProtocolEndpoints.  # noqa: E501
        :type: ProtocolEndpoint
        """

        self._sso = sso

    @property
    def token(self):
        """Gets the token of this ProtocolEndpoints.  # noqa: E501


        :return: The token of this ProtocolEndpoints.  # noqa: E501
        :rtype: ProtocolEndpoint
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this ProtocolEndpoints.


        :param token: The token of this ProtocolEndpoints.  # noqa: E501
        :type: ProtocolEndpoint
        """

        self._token = token

    @property
    def user_info(self):
        """Gets the user_info of this ProtocolEndpoints.  # noqa: E501


        :return: The user_info of this ProtocolEndpoints.  # noqa: E501
        :rtype: ProtocolEndpoint
        """
        return self._user_info

    @user_info.setter
    def user_info(self, user_info):
        """Sets the user_info of this ProtocolEndpoints.


        :param user_info: The user_info of this ProtocolEndpoints.  # noqa: E501
        :type: ProtocolEndpoint
        """

        self._user_info = user_info

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
        if issubclass(ProtocolEndpoints, dict):
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
        if not isinstance(other, ProtocolEndpoints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
