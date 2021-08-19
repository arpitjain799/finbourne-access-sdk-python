# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1322
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class AsAtPredicateContract(object):
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
        'value': 'str',
        'date_time_offset': 'datetime'
    }

    attribute_map = {
        'value': 'value',
        'date_time_offset': 'dateTimeOffset'
    }

    required_map = {
        'value': 'optional',
        'date_time_offset': 'optional'
    }

    def __init__(self, value=None, date_time_offset=None):  # noqa: E501
        """
        AsAtPredicateContract - a model defined in OpenAPI

        :param value: 
        :type value: str
        :param date_time_offset: 
        :type date_time_offset: datetime

        """  # noqa: E501

        self._value = None
        self._date_time_offset = None
        self.discriminator = None

        self.value = value
        self.date_time_offset = date_time_offset

    @property
    def value(self):
        """Gets the value of this AsAtPredicateContract.  # noqa: E501


        :return: The value of this AsAtPredicateContract.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AsAtPredicateContract.


        :param value: The value of this AsAtPredicateContract.  # noqa: E501
        :type: str
        """
        if value is not None and len(value) > 25:
            raise ValueError("Invalid value for `value`, length must be less than or equal to `25`")  # noqa: E501
        if value is not None and len(value) < 5:
            raise ValueError("Invalid value for `value`, length must be greater than or equal to `5`")  # noqa: E501

        self._value = value

    @property
    def date_time_offset(self):
        """Gets the date_time_offset of this AsAtPredicateContract.  # noqa: E501


        :return: The date_time_offset of this AsAtPredicateContract.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time_offset

    @date_time_offset.setter
    def date_time_offset(self, date_time_offset):
        """Sets the date_time_offset of this AsAtPredicateContract.


        :param date_time_offset: The date_time_offset of this AsAtPredicateContract.  # noqa: E501
        :type: datetime
        """

        self._date_time_offset = date_time_offset

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
        if not isinstance(other, AsAtPredicateContract):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
