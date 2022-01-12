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

class User(object):
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
    swagger_types['embedded'] = 'dict(str, object)'
    swagger_types['links'] = 'dict(str, object)'
    swagger_types['activated'] = 'datetime'
    swagger_types['created'] = 'datetime'
    swagger_types['credentials'] = 'UserCredentials'
    swagger_types['id'] = 'str'
    swagger_types['last_login'] = 'datetime'
    swagger_types['last_updated'] = 'datetime'
    swagger_types['password_changed'] = 'datetime'
    swagger_types['profile'] = 'UserProfile'
    swagger_types['status'] = 'UserStatus'
    swagger_types['status_changed'] = 'datetime'
    swagger_types['transitioning_to_status'] = 'UserStatus'
    swagger_types['type'] = 'UserType'

    attribute_map = {
        'embedded': '_embedded',
        'links': '_links',
        'activated': 'activated',
        'created': 'created',
        'credentials': 'credentials',
        'id': 'id',
        'last_login': 'lastLogin',
        'last_updated': 'lastUpdated',
        'password_changed': 'passwordChanged',
        'profile': 'profile',
        'status': 'status',
        'status_changed': 'statusChanged',
        'transitioning_to_status': 'transitioningToStatus',
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

    def set_attributes(self, embedded=None, links=None, activated=None, created=None, credentials=None, id=None, last_login=None, last_updated=None, password_changed=None, profile=None, status=None, status_changed=None, transitioning_to_status=None, type=None, **kwargs):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501
        self._embedded = None
        self._links = None
        self._activated = None
        self._created = None
        self._credentials = None
        self._id = None
        self._last_login = None
        self._last_updated = None
        self._password_changed = None
        self._profile = None
        self._status = None
        self._status_changed = None
        self._transitioning_to_status = None
        self._type = None
        self.discriminator = None
        if embedded is not None:
            if hasattr(models, self.swagger_types['embedded']):
                nested_class = getattr(models, self.swagger_types['embedded'])
                if isinstance(embedded, nested_class):
                    self.embedded = embedded
                elif isinstance(embedded, dict):
                    self.embedded = nested_class.from_kwargs(**embedded)
                else:
                    self.embedded = embedded
            else:
                self.embedded = embedded
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
        if activated is not None:
            if hasattr(models, self.swagger_types['activated']):
                nested_class = getattr(models, self.swagger_types['activated'])
                if isinstance(activated, nested_class):
                    self.activated = activated
                elif isinstance(activated, dict):
                    self.activated = nested_class.from_kwargs(**activated)
                else:
                    self.activated = activated
            else:
                self.activated = activated
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
        if last_login is not None:
            if hasattr(models, self.swagger_types['last_login']):
                nested_class = getattr(models, self.swagger_types['last_login'])
                if isinstance(last_login, nested_class):
                    self.last_login = last_login
                elif isinstance(last_login, dict):
                    self.last_login = nested_class.from_kwargs(**last_login)
                else:
                    self.last_login = last_login
            else:
                self.last_login = last_login
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
        if password_changed is not None:
            if hasattr(models, self.swagger_types['password_changed']):
                nested_class = getattr(models, self.swagger_types['password_changed'])
                if isinstance(password_changed, nested_class):
                    self.password_changed = password_changed
                elif isinstance(password_changed, dict):
                    self.password_changed = nested_class.from_kwargs(**password_changed)
                else:
                    self.password_changed = password_changed
            else:
                self.password_changed = password_changed
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
        if status_changed is not None:
            if hasattr(models, self.swagger_types['status_changed']):
                nested_class = getattr(models, self.swagger_types['status_changed'])
                if isinstance(status_changed, nested_class):
                    self.status_changed = status_changed
                elif isinstance(status_changed, dict):
                    self.status_changed = nested_class.from_kwargs(**status_changed)
                else:
                    self.status_changed = status_changed
            else:
                self.status_changed = status_changed
        if transitioning_to_status is not None:
            if hasattr(models, self.swagger_types['transitioning_to_status']):
                nested_class = getattr(models, self.swagger_types['transitioning_to_status'])
                if isinstance(transitioning_to_status, nested_class):
                    self.transitioning_to_status = transitioning_to_status
                elif isinstance(transitioning_to_status, dict):
                    self.transitioning_to_status = nested_class.from_kwargs(**transitioning_to_status)
                else:
                    self.transitioning_to_status = transitioning_to_status
            else:
                self.transitioning_to_status = transitioning_to_status
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
    def embedded(self):
        """Gets the embedded of this User.  # noqa: E501


        :return: The embedded of this User.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this User.


        :param embedded: The embedded of this User.  # noqa: E501
        :type: dict(str, object)
        """

        self._embedded = embedded

    @property
    def links(self):
        """Gets the links of this User.  # noqa: E501


        :return: The links of this User.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this User.


        :param links: The links of this User.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

    @property
    def activated(self):
        """Gets the activated of this User.  # noqa: E501


        :return: The activated of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._activated

    @activated.setter
    def activated(self, activated):
        """Sets the activated of this User.


        :param activated: The activated of this User.  # noqa: E501
        :type: datetime
        """

        self._activated = activated

    @property
    def created(self):
        """Gets the created of this User.  # noqa: E501


        :return: The created of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this User.


        :param created: The created of this User.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def credentials(self):
        """Gets the credentials of this User.  # noqa: E501


        :return: The credentials of this User.  # noqa: E501
        :rtype: UserCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this User.


        :param credentials: The credentials of this User.  # noqa: E501
        :type: UserCredentials
        """

        self._credentials = credentials

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501


        :return: The id of this User.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.


        :param id: The id of this User.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_login(self):
        """Gets the last_login of this User.  # noqa: E501


        :return: The last_login of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._last_login

    @last_login.setter
    def last_login(self, last_login):
        """Sets the last_login of this User.


        :param last_login: The last_login of this User.  # noqa: E501
        :type: datetime
        """

        self._last_login = last_login

    @property
    def last_updated(self):
        """Gets the last_updated of this User.  # noqa: E501


        :return: The last_updated of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this User.


        :param last_updated: The last_updated of this User.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def password_changed(self):
        """Gets the password_changed of this User.  # noqa: E501


        :return: The password_changed of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._password_changed

    @password_changed.setter
    def password_changed(self, password_changed):
        """Sets the password_changed of this User.


        :param password_changed: The password_changed of this User.  # noqa: E501
        :type: datetime
        """

        self._password_changed = password_changed

    @property
    def profile(self):
        """Gets the profile of this User.  # noqa: E501


        :return: The profile of this User.  # noqa: E501
        :rtype: UserProfile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this User.


        :param profile: The profile of this User.  # noqa: E501
        :type: UserProfile
        """

        self._profile = profile

    @property
    def status(self):
        """Gets the status of this User.  # noqa: E501


        :return: The status of this User.  # noqa: E501
        :rtype: UserStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this User.


        :param status: The status of this User.  # noqa: E501
        :type: UserStatus
        """

        self._status = status

    @property
    def status_changed(self):
        """Gets the status_changed of this User.  # noqa: E501


        :return: The status_changed of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._status_changed

    @status_changed.setter
    def status_changed(self, status_changed):
        """Sets the status_changed of this User.


        :param status_changed: The status_changed of this User.  # noqa: E501
        :type: datetime
        """

        self._status_changed = status_changed

    @property
    def transitioning_to_status(self):
        """Gets the transitioning_to_status of this User.  # noqa: E501


        :return: The transitioning_to_status of this User.  # noqa: E501
        :rtype: UserStatus
        """
        return self._transitioning_to_status

    @transitioning_to_status.setter
    def transitioning_to_status(self, transitioning_to_status):
        """Sets the transitioning_to_status of this User.


        :param transitioning_to_status: The transitioning_to_status of this User.  # noqa: E501
        :type: UserStatus
        """

        self._transitioning_to_status = transitioning_to_status

    @property
    def type(self):
        """Gets the type of this User.  # noqa: E501


        :return: The type of this User.  # noqa: E501
        :rtype: UserType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this User.


        :param type: The type of this User.  # noqa: E501
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
        if issubclass(User, dict):
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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
