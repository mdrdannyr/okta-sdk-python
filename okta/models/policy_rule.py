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

class PolicyRule(object):
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
    swagger_types['created'] = 'datetime'
    swagger_types['id'] = 'str'
    swagger_types['last_updated'] = 'datetime'
    swagger_types['priority'] = 'int'
    swagger_types['status'] = 'LifecycleStatus'
    swagger_types['system'] = 'bool'
    swagger_types['type'] = 'PolicyRuleType'
    swagger_types['name'] = 'str'
    swagger_types['conditions'] = 'PolicyRuleConditions'
    swagger_types['actions'] = 'PolicyRuleActions'

    attribute_map = {
        'created': 'created',
        'id': 'id',
        'last_updated': 'lastUpdated',
        'priority': 'priority',
        'status': 'status',
        'system': 'system',
        'type': 'type',
        'name': 'name',
        'conditions': 'conditions',
        'actions': 'actions'
    }

    discriminator_value_class_map = {
            'ACCESS_POLICY'.lower(): 'AccessPolicyRule',
            'PASSWORD'.lower(): 'PasswordPolicyRule',
            'PROFILE_ENROLLMENT'.lower(): 'ProfileEnrollmentPolicyRule',
            'SIGN_ON'.lower(): 'OktaSignOnPolicyRule',
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

    def set_attributes(self, created=None, id=None, last_updated=None, priority=None, status=None, system=False, type=None, name=None, conditions=None, actions=None, **kwargs):  # noqa: E501
        """PolicyRule - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._id = None
        self._last_updated = None
        self._priority = None
        self._status = None
        self._system = None
        self._type = None
        self._name = None
        self._conditions = None
        self._actions = None
        self.discriminator = 'type'
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
        if priority is not None:
            if hasattr(models, self.swagger_types['priority']):
                nested_class = getattr(models, self.swagger_types['priority'])
                if isinstance(priority, nested_class):
                    self.priority = priority
                elif isinstance(priority, dict):
                    self.priority = nested_class.from_kwargs(**priority)
                else:
                    self.priority = priority
            else:
                self.priority = priority
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
        if system is not None:
            if hasattr(models, self.swagger_types['system']):
                nested_class = getattr(models, self.swagger_types['system'])
                if isinstance(system, nested_class):
                    self.system = system
                elif isinstance(system, dict):
                    self.system = nested_class.from_kwargs(**system)
                else:
                    self.system = system
            else:
                self.system = system
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
        if conditions is not None:
            if hasattr(models, self.swagger_types['conditions']):
                nested_class = getattr(models, self.swagger_types['conditions'])
                if isinstance(conditions, nested_class):
                    self.conditions = conditions
                elif isinstance(conditions, dict):
                    self.conditions = nested_class.from_kwargs(**conditions)
                else:
                    self.conditions = conditions
            else:
                self.conditions = conditions
        if actions is not None:
            if hasattr(models, self.swagger_types['actions']):
                nested_class = getattr(models, self.swagger_types['actions'])
                if isinstance(actions, nested_class):
                    self.actions = actions
                elif isinstance(actions, dict):
                    self.actions = nested_class.from_kwargs(**actions)
                else:
                    self.actions = actions
            else:
                self.actions = actions

    @property
    def created(self):
        """Gets the created of this PolicyRule.  # noqa: E501


        :return: The created of this PolicyRule.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PolicyRule.


        :param created: The created of this PolicyRule.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def id(self):
        """Gets the id of this PolicyRule.  # noqa: E501


        :return: The id of this PolicyRule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PolicyRule.


        :param id: The id of this PolicyRule.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_updated(self):
        """Gets the last_updated of this PolicyRule.  # noqa: E501


        :return: The last_updated of this PolicyRule.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this PolicyRule.


        :param last_updated: The last_updated of this PolicyRule.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def priority(self):
        """Gets the priority of this PolicyRule.  # noqa: E501


        :return: The priority of this PolicyRule.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this PolicyRule.


        :param priority: The priority of this PolicyRule.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def status(self):
        """Gets the status of this PolicyRule.  # noqa: E501


        :return: The status of this PolicyRule.  # noqa: E501
        :rtype: LifecycleStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PolicyRule.


        :param status: The status of this PolicyRule.  # noqa: E501
        :type: LifecycleStatus
        """

        self._status = status

    @property
    def system(self):
        """Gets the system of this PolicyRule.  # noqa: E501


        :return: The system of this PolicyRule.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this PolicyRule.


        :param system: The system of this PolicyRule.  # noqa: E501
        :type: bool
        """

        self._system = system

    @property
    def type(self):
        """Gets the type of this PolicyRule.  # noqa: E501


        :return: The type of this PolicyRule.  # noqa: E501
        :rtype: PolicyRuleType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PolicyRule.


        :param type: The type of this PolicyRule.  # noqa: E501
        :type: PolicyRuleType
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this PolicyRule.  # noqa: E501


        :return: The name of this PolicyRule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PolicyRule.


        :param name: The name of this PolicyRule.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def conditions(self):
        """Gets the conditions of this PolicyRule.  # noqa: E501


        :return: The conditions of this PolicyRule.  # noqa: E501
        :rtype: PolicyRuleConditions
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this PolicyRule.


        :param conditions: The conditions of this PolicyRule.  # noqa: E501
        :type: PolicyRuleConditions
        """

        self._conditions = conditions

    @property
    def actions(self):
        """Gets the actions of this PolicyRule.  # noqa: E501


        :return: The actions of this PolicyRule.  # noqa: E501
        :rtype: PolicyRuleActions
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this PolicyRule.


        :param actions: The actions of this PolicyRule.  # noqa: E501
        :type: PolicyRuleActions
        """

        self._actions = actions

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(PolicyRule, dict):
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
        if not isinstance(other, PolicyRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
