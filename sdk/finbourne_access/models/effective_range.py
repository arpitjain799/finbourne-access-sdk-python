# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1336
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class EffectiveRange(object):
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
        '_from': 'datetime',
        'to': 'datetime'
    }

    attribute_map = {
        '_from': 'from',
        'to': 'to'
    }

    required_map = {
        '_from': 'optional',
        'to': 'optional'
    }

    def __init__(self, _from=None, to=None):  # noqa: E501
        """
        EffectiveRange - a model defined in OpenAPI

        :param _from: 
        :type _from: datetime
        :param to: 
        :type to: datetime

        """  # noqa: E501

        self.__from = None
        self._to = None
        self.discriminator = None

        if _from is not None:
            self._from = _from
        self.to = to

    @property
    def _from(self):
        """Gets the _from of this EffectiveRange.  # noqa: E501


        :return: The _from of this EffectiveRange.  # noqa: E501
        :rtype: datetime
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this EffectiveRange.


        :param _from: The _from of this EffectiveRange.  # noqa: E501
        :type: datetime
        """

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this EffectiveRange.  # noqa: E501


        :return: The to of this EffectiveRange.  # noqa: E501
        :rtype: datetime
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this EffectiveRange.


        :param to: The to of this EffectiveRange.  # noqa: E501
        :type: datetime
        """

        self._to = to

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EffectiveRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
