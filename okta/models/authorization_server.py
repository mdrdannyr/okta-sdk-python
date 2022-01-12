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

class AuthorizationServer(object):
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
    swagger_types['audiences'] = 'list[str]'
    swagger_types['created'] = 'datetime'
    swagger_types['credentials'] = 'AuthorizationServerCredentials'
    swagger_types['description'] = 'str'
    swagger_types['id'] = 'str'
    swagger_types['issuer'] = 'str'
    swagger_types['issuer_mode'] = 'IssuerMode'
    swagger_types['last_updated'] = 'datetime'
    swagger_types['name'] = 'str'
    swagger_types['status'] = 'LifecycleStatus'

    attribute_map = {
        'links': '_links',
        'audiences': 'audiences',
        'created': 'created',
        'credentials': 'credentials',
        'description': 'description',
        'id': 'id',
        'issuer': 'issuer',
        'issuer_mode': 'issuerMode',
        'last_updated': 'lastUpdated',
        'name': 'name',
        'status': 'status'
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

    def set_attributes(self, links=None, audiences=None, created=None, credentials=None, description=None, id=None, issuer=None, issuer_mode=None, last_updated=None, name=None, status=None, **kwargs):  # noqa: E501
        """AuthorizationServer - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self._audiences = None
        self._created = None
        self._credentials = None
        self._description = None
        self._id = None
        self._issuer = None
        self._issuer_mode = None
        self._last_updated = None
        self._name = None
        self._status = None
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
        if audiences is not None:
            if hasattr(models, self.swagger_types['audiences']):
                nested_class = getattr(models, self.swagger_types['audiences'])
                if isinstance(audiences, nested_class):
                    self.audiences = audiences
                elif isinstance(audiences, dict):
                    self.audiences = nested_class.from_kwargs(**audiences)
                else:
                    self.audiences = audiences
            else:
                self.audiences = audiences
        if created is not None:
            if hasattr(models, self.swagger_types['created']):
                nested_class = getattr(models, self.swagger_types['created'])
                if isinstance(created, nested_class):
                    self.created = created
                elif isinstance(created, dict):
                    self.created = nested_class.from_kwargs(**created)
                else:
                    self.created = created
            else:
                self.created = created
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
        if description is not None:
            if hasattr(models, self.swagger_types['description']):
                nested_class = getattr(models, self.swagger_types['description'])
                if isinstance(description, nested_class):
                    self.description = description
                elif isinstance(description, dict):
                    self.description = nested_class.from_kwargs(**description)
                else:
                    self.description = description
            else:
                self.description = description
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
        if issuer is not None:
            if hasattr(models, self.swagger_types['issuer']):
                nested_class = getattr(models, self.swagger_types['issuer'])
                if isinstance(issuer, nested_class):
                    self.issuer = issuer
                elif isinstance(issuer, dict):
                    self.issuer = nested_class.from_kwargs(**issuer)
                else:
                    self.issuer = issuer
            else:
                self.issuer = issuer
        if issuer_mode is not None:
            if hasattr(models, self.swagger_types['issuer_mode']):
                nested_class = getattr(models, self.swagger_types['issuer_mode'])
                if isinstance(issuer_mode, nested_class):
                    self.issuer_mode = issuer_mode
                elif isinstance(issuer_mode, dict):
                    self.issuer_mode = nested_class.from_kwargs(**issuer_mode)
                else:
                    self.issuer_mode = issuer_mode
            else:
                self.issuer_mode = issuer_mode
        if last_updated is not None:
            if hasattr(models, self.swagger_types['last_updated']):
                nested_class = getattr(models, self.swagger_types['last_updated'])
                if isinstance(last_updated, nested_class):
                    self.last_updated = last_updated
                elif isinstance(last_updated, dict):
                    self.last_updated = nested_class.from_kwargs(**last_updated)
                else:
                    self.last_updated = last_updated
            else:
                self.last_updated = last_updated
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
        if status is not None:
            if hasattr(models, self.swagger_types['status']):
                nested_class = getattr(models, self.swagger_types['status'])
                if isinstance(status, nested_class):
                    self.status = status
                elif isinstance(status, dict):
                    self.status = nested_class.from_kwargs(**status)
                else:
                    self.status = status
            else:
                self.status = status

    @property
    def links(self):
        """Gets the links of this AuthorizationServer.  # noqa: E501


        :return: The links of this AuthorizationServer.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AuthorizationServer.


        :param links: The links of this AuthorizationServer.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

    @property
    def audiences(self):
        """Gets the audiences of this AuthorizationServer.  # noqa: E501


        :return: The audiences of this AuthorizationServer.  # noqa: E501
        :rtype: list[str]
        """
        return self._audiences

    @audiences.setter
    def audiences(self, audiences):
        """Sets the audiences of this AuthorizationServer.


        :param audiences: The audiences of this AuthorizationServer.  # noqa: E501
        :type: list[str]
        """

        self._audiences = audiences

    @property
    def created(self):
        """Gets the created of this AuthorizationServer.  # noqa: E501


        :return: The created of this AuthorizationServer.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this AuthorizationServer.


        :param created: The created of this AuthorizationServer.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def credentials(self):
        """Gets the credentials of this AuthorizationServer.  # noqa: E501


        :return: The credentials of this AuthorizationServer.  # noqa: E501
        :rtype: AuthorizationServerCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this AuthorizationServer.


        :param credentials: The credentials of this AuthorizationServer.  # noqa: E501
        :type: AuthorizationServerCredentials
        """

        self._credentials = credentials

    @property
    def description(self):
        """Gets the description of this AuthorizationServer.  # noqa: E501


        :return: The description of this AuthorizationServer.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AuthorizationServer.


        :param description: The description of this AuthorizationServer.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this AuthorizationServer.  # noqa: E501


        :return: The id of this AuthorizationServer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuthorizationServer.


        :param id: The id of this AuthorizationServer.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def issuer(self):
        """Gets the issuer of this AuthorizationServer.  # noqa: E501


        :return: The issuer of this AuthorizationServer.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this AuthorizationServer.


        :param issuer: The issuer of this AuthorizationServer.  # noqa: E501
        :type: str
        """

        self._issuer = issuer

    @property
    def issuer_mode(self):
        """Gets the issuer_mode of this AuthorizationServer.  # noqa: E501


        :return: The issuer_mode of this AuthorizationServer.  # noqa: E501
        :rtype: IssuerMode
        """
        return self._issuer_mode

    @issuer_mode.setter
    def issuer_mode(self, issuer_mode):
        """Sets the issuer_mode of this AuthorizationServer.


        :param issuer_mode: The issuer_mode of this AuthorizationServer.  # noqa: E501
        :type: IssuerMode
        """

        self._issuer_mode = issuer_mode

    @property
    def last_updated(self):
        """Gets the last_updated of this AuthorizationServer.  # noqa: E501


        :return: The last_updated of this AuthorizationServer.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this AuthorizationServer.


        :param last_updated: The last_updated of this AuthorizationServer.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def name(self):
        """Gets the name of this AuthorizationServer.  # noqa: E501


        :return: The name of this AuthorizationServer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuthorizationServer.


        :param name: The name of this AuthorizationServer.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this AuthorizationServer.  # noqa: E501


        :return: The status of this AuthorizationServer.  # noqa: E501
        :rtype: LifecycleStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AuthorizationServer.


        :param status: The status of this AuthorizationServer.  # noqa: E501
        :type: LifecycleStatus
        """

        self._status = status

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
        if issubclass(AuthorizationServer, dict):
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
        if not isinstance(other, AuthorizationServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
