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
from okta.models.application_settings_application import ApplicationSettingsApplication  # noqa: F401,E501

import okta.models as models  # noqa
from okta.helpers import to_snake_case

class SwaApplicationSettingsApplication(ApplicationSettingsApplication):
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
    if hasattr(ApplicationSettingsApplication, "swagger_types"):
        swagger_types.update(ApplicationSettingsApplication.swagger_types)
    swagger_types['button_field'] = 'str'
    swagger_types['checkbox'] = 'str'
    swagger_types['login_url_regex'] = 'str'
    swagger_types['password_field'] = 'str'
    swagger_types['redirect_url'] = 'str'
    swagger_types['url'] = 'str'
    swagger_types['username_field'] = 'str'

    attribute_map = {
        'button_field': 'buttonField',
        'checkbox': 'checkbox',
        'login_url_regex': 'loginUrlRegex',
        'password_field': 'passwordField',
        'redirect_url': 'redirectUrl',
        'url': 'url',
        'username_field': 'usernameField'
    }
    if hasattr(ApplicationSettingsApplication, "attribute_map"):
        attribute_map.update(ApplicationSettingsApplication.attribute_map)

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
        else:
            config = {}
        self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, button_field=None, checkbox=None, login_url_regex=None, password_field=None, redirect_url=None, url=None, username_field=None, **kwargs):  # noqa: E501
        """SwaApplicationSettingsApplication - a model defined in Swagger"""  # noqa: E501
        config = {}
        if kwargs is not None:
            config = {to_snake_case(key): value for key, value in kwargs.items()}
        super().set_attributes(**config)
        self._button_field = None
        self._checkbox = None
        self._login_url_regex = None
        self._password_field = None
        self._redirect_url = None
        self._url = None
        self._username_field = None
        self.discriminator = None
        if button_field is not None:
            if hasattr(models, self.swagger_types['button_field']):
                nested_class = getattr(models, self.swagger_types['button_field'])
                if isinstance(button_field, nested_class):
                    self.button_field = button_field
                elif isinstance(button_field, dict):
                    self.button_field = nested_class.from_kwargs(**button_field)
                else:
                    self.button_field = button_field
            else:
                self.button_field = button_field
        if checkbox is not None:
            if hasattr(models, self.swagger_types['checkbox']):
                nested_class = getattr(models, self.swagger_types['checkbox'])
                if isinstance(checkbox, nested_class):
                    self.checkbox = checkbox
                elif isinstance(checkbox, dict):
                    self.checkbox = nested_class.from_kwargs(**checkbox)
                else:
                    self.checkbox = checkbox
            else:
                self.checkbox = checkbox
        if login_url_regex is not None:
            if hasattr(models, self.swagger_types['login_url_regex']):
                nested_class = getattr(models, self.swagger_types['login_url_regex'])
                if isinstance(login_url_regex, nested_class):
                    self.login_url_regex = login_url_regex
                elif isinstance(login_url_regex, dict):
                    self.login_url_regex = nested_class.from_kwargs(**login_url_regex)
                else:
                    self.login_url_regex = login_url_regex
            else:
                self.login_url_regex = login_url_regex
        if password_field is not None:
            if hasattr(models, self.swagger_types['password_field']):
                nested_class = getattr(models, self.swagger_types['password_field'])
                if isinstance(password_field, nested_class):
                    self.password_field = password_field
                elif isinstance(password_field, dict):
                    self.password_field = nested_class.from_kwargs(**password_field)
                else:
                    self.password_field = password_field
            else:
                self.password_field = password_field
        if redirect_url is not None:
            if hasattr(models, self.swagger_types['redirect_url']):
                nested_class = getattr(models, self.swagger_types['redirect_url'])
                if isinstance(redirect_url, nested_class):
                    self.redirect_url = redirect_url
                elif isinstance(redirect_url, dict):
                    self.redirect_url = nested_class.from_kwargs(**redirect_url)
                else:
                    self.redirect_url = redirect_url
            else:
                self.redirect_url = redirect_url
        if url is not None:
            if hasattr(models, self.swagger_types['url']):
                nested_class = getattr(models, self.swagger_types['url'])
                if isinstance(url, nested_class):
                    self.url = url
                elif isinstance(url, dict):
                    self.url = nested_class.from_kwargs(**url)
                else:
                    self.url = url
            else:
                self.url = url
        if username_field is not None:
            if hasattr(models, self.swagger_types['username_field']):
                nested_class = getattr(models, self.swagger_types['username_field'])
                if isinstance(username_field, nested_class):
                    self.username_field = username_field
                elif isinstance(username_field, dict):
                    self.username_field = nested_class.from_kwargs(**username_field)
                else:
                    self.username_field = username_field
            else:
                self.username_field = username_field

    @property
    def button_field(self):
        """Gets the button_field of this SwaApplicationSettingsApplication.  # noqa: E501


        :return: The button_field of this SwaApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._button_field

    @button_field.setter
    def button_field(self, button_field):
        """Sets the button_field of this SwaApplicationSettingsApplication.


        :param button_field: The button_field of this SwaApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._button_field = button_field

    @property
    def checkbox(self):
        """Gets the checkbox of this SwaApplicationSettingsApplication.  # noqa: E501


        :return: The checkbox of this SwaApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._checkbox

    @checkbox.setter
    def checkbox(self, checkbox):
        """Sets the checkbox of this SwaApplicationSettingsApplication.


        :param checkbox: The checkbox of this SwaApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._checkbox = checkbox

    @property
    def login_url_regex(self):
        """Gets the login_url_regex of this SwaApplicationSettingsApplication.  # noqa: E501


        :return: The login_url_regex of this SwaApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._login_url_regex

    @login_url_regex.setter
    def login_url_regex(self, login_url_regex):
        """Sets the login_url_regex of this SwaApplicationSettingsApplication.


        :param login_url_regex: The login_url_regex of this SwaApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._login_url_regex = login_url_regex

    @property
    def password_field(self):
        """Gets the password_field of this SwaApplicationSettingsApplication.  # noqa: E501


        :return: The password_field of this SwaApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._password_field

    @password_field.setter
    def password_field(self, password_field):
        """Sets the password_field of this SwaApplicationSettingsApplication.


        :param password_field: The password_field of this SwaApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._password_field = password_field

    @property
    def redirect_url(self):
        """Gets the redirect_url of this SwaApplicationSettingsApplication.  # noqa: E501


        :return: The redirect_url of this SwaApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this SwaApplicationSettingsApplication.


        :param redirect_url: The redirect_url of this SwaApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._redirect_url = redirect_url

    @property
    def url(self):
        """Gets the url of this SwaApplicationSettingsApplication.  # noqa: E501


        :return: The url of this SwaApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SwaApplicationSettingsApplication.


        :param url: The url of this SwaApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def username_field(self):
        """Gets the username_field of this SwaApplicationSettingsApplication.  # noqa: E501


        :return: The username_field of this SwaApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._username_field

    @username_field.setter
    def username_field(self, username_field):
        """Sets the username_field of this SwaApplicationSettingsApplication.


        :param username_field: The username_field of this SwaApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._username_field = username_field

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
        if issubclass(SwaApplicationSettingsApplication, dict):
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
        if not isinstance(other, SwaApplicationSettingsApplication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
