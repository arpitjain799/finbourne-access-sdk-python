# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.2696
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from finbourne_access.configuration import Configuration


class UserRoleCreationRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'user_id': 'str',
        'resource': 'PolicyIdRoleResource'
    }

    attribute_map = {
        'user_id': 'userId',
        'resource': 'resource'
    }

    required_map = {
        'user_id': 'required',
        'resource': 'required'
    }

    def __init__(self, user_id=None, resource=None, local_vars_configuration=None):  # noqa: E501
        """UserRoleCreationRequest - a model defined in OpenAPI"
        
        :param user_id:  The Id of the user for whom to create the role. (required)
        :type user_id: str
        :param resource:  (required)
        :type resource: finbourne_access.PolicyIdRoleResource

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._user_id = None
        self._resource = None
        self.discriminator = None

        self.user_id = user_id
        self.resource = resource

    @property
    def user_id(self):
        """Gets the user_id of this UserRoleCreationRequest.  # noqa: E501

        The Id of the user for whom to create the role.  # noqa: E501

        :return: The user_id of this UserRoleCreationRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserRoleCreationRequest.

        The Id of the user for whom to create the role.  # noqa: E501

        :param user_id: The user_id of this UserRoleCreationRequest.  # noqa: E501
        :type user_id: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                user_id is not None and not re.search(r'^(?=.*[a-zA-Z])[\w][\w +-]{2,100}$', user_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `user_id`, must be a follow pattern or equal to `/^(?=.*[a-zA-Z])[\w][\w +-]{2,100}$/`")  # noqa: E501

        self._user_id = user_id

    @property
    def resource(self):
        """Gets the resource of this UserRoleCreationRequest.  # noqa: E501


        :return: The resource of this UserRoleCreationRequest.  # noqa: E501
        :rtype: finbourne_access.PolicyIdRoleResource
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this UserRoleCreationRequest.


        :param resource: The resource of this UserRoleCreationRequest.  # noqa: E501
        :type resource: finbourne_access.PolicyIdRoleResource
        """
        if self.local_vars_configuration.client_side_validation and resource is None:  # noqa: E501
            raise ValueError("Invalid value for `resource`, must not be `None`")  # noqa: E501

        self._resource = resource

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserRoleCreationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserRoleCreationRequest):
            return True

        return self.to_dict() != other.to_dict()
