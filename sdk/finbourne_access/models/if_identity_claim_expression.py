# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.2947
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


class IfIdentityClaimExpression(object):
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
        'claim_type': 'str',
        'claim_value_type': 'str',
        'claim_issuer': 'str',
        'claim_original_issuer': 'str',
        'operator': 'TextOperator',
        'value': 'str'
    }

    attribute_map = {
        'claim_type': 'claimType',
        'claim_value_type': 'claimValueType',
        'claim_issuer': 'claimIssuer',
        'claim_original_issuer': 'claimOriginalIssuer',
        'operator': 'operator',
        'value': 'value'
    }

    required_map = {
        'claim_type': 'required',
        'claim_value_type': 'required',
        'claim_issuer': 'optional',
        'claim_original_issuer': 'optional',
        'operator': 'required',
        'value': 'optional'
    }

    def __init__(self, claim_type=None, claim_value_type=None, claim_issuer=None, claim_original_issuer=None, operator=None, value=None, local_vars_configuration=None):  # noqa: E501
        """IfIdentityClaimExpression - a model defined in OpenAPI"
        
        :param claim_type:  (required)
        :type claim_type: str
        :param claim_value_type:  (required)
        :type claim_value_type: str
        :param claim_issuer: 
        :type claim_issuer: str
        :param claim_original_issuer: 
        :type claim_original_issuer: str
        :param operator:  (required)
        :type operator: finbourne_access.TextOperator
        :param value: 
        :type value: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._claim_type = None
        self._claim_value_type = None
        self._claim_issuer = None
        self._claim_original_issuer = None
        self._operator = None
        self._value = None
        self.discriminator = None

        self.claim_type = claim_type
        self.claim_value_type = claim_value_type
        self.claim_issuer = claim_issuer
        self.claim_original_issuer = claim_original_issuer
        self.operator = operator
        self.value = value

    @property
    def claim_type(self):
        """Gets the claim_type of this IfIdentityClaimExpression.  # noqa: E501


        :return: The claim_type of this IfIdentityClaimExpression.  # noqa: E501
        :rtype: str
        """
        return self._claim_type

    @claim_type.setter
    def claim_type(self, claim_type):
        """Sets the claim_type of this IfIdentityClaimExpression.


        :param claim_type: The claim_type of this IfIdentityClaimExpression.  # noqa: E501
        :type claim_type: str
        """
        if self.local_vars_configuration.client_side_validation and claim_type is None:  # noqa: E501
            raise ValueError("Invalid value for `claim_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                claim_type is not None and len(claim_type) < 1):
            raise ValueError("Invalid value for `claim_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._claim_type = claim_type

    @property
    def claim_value_type(self):
        """Gets the claim_value_type of this IfIdentityClaimExpression.  # noqa: E501


        :return: The claim_value_type of this IfIdentityClaimExpression.  # noqa: E501
        :rtype: str
        """
        return self._claim_value_type

    @claim_value_type.setter
    def claim_value_type(self, claim_value_type):
        """Sets the claim_value_type of this IfIdentityClaimExpression.


        :param claim_value_type: The claim_value_type of this IfIdentityClaimExpression.  # noqa: E501
        :type claim_value_type: str
        """
        if self.local_vars_configuration.client_side_validation and claim_value_type is None:  # noqa: E501
            raise ValueError("Invalid value for `claim_value_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                claim_value_type is not None and len(claim_value_type) < 1):
            raise ValueError("Invalid value for `claim_value_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._claim_value_type = claim_value_type

    @property
    def claim_issuer(self):
        """Gets the claim_issuer of this IfIdentityClaimExpression.  # noqa: E501


        :return: The claim_issuer of this IfIdentityClaimExpression.  # noqa: E501
        :rtype: str
        """
        return self._claim_issuer

    @claim_issuer.setter
    def claim_issuer(self, claim_issuer):
        """Sets the claim_issuer of this IfIdentityClaimExpression.


        :param claim_issuer: The claim_issuer of this IfIdentityClaimExpression.  # noqa: E501
        :type claim_issuer: str
        """

        self._claim_issuer = claim_issuer

    @property
    def claim_original_issuer(self):
        """Gets the claim_original_issuer of this IfIdentityClaimExpression.  # noqa: E501


        :return: The claim_original_issuer of this IfIdentityClaimExpression.  # noqa: E501
        :rtype: str
        """
        return self._claim_original_issuer

    @claim_original_issuer.setter
    def claim_original_issuer(self, claim_original_issuer):
        """Sets the claim_original_issuer of this IfIdentityClaimExpression.


        :param claim_original_issuer: The claim_original_issuer of this IfIdentityClaimExpression.  # noqa: E501
        :type claim_original_issuer: str
        """

        self._claim_original_issuer = claim_original_issuer

    @property
    def operator(self):
        """Gets the operator of this IfIdentityClaimExpression.  # noqa: E501


        :return: The operator of this IfIdentityClaimExpression.  # noqa: E501
        :rtype: finbourne_access.TextOperator
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this IfIdentityClaimExpression.


        :param operator: The operator of this IfIdentityClaimExpression.  # noqa: E501
        :type operator: finbourne_access.TextOperator
        """
        if self.local_vars_configuration.client_side_validation and operator is None:  # noqa: E501
            raise ValueError("Invalid value for `operator`, must not be `None`")  # noqa: E501

        self._operator = operator

    @property
    def value(self):
        """Gets the value of this IfIdentityClaimExpression.  # noqa: E501


        :return: The value of this IfIdentityClaimExpression.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this IfIdentityClaimExpression.


        :param value: The value of this IfIdentityClaimExpression.  # noqa: E501
        :type value: str
        """

        self._value = value

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
        if not isinstance(other, IfIdentityClaimExpression):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IfIdentityClaimExpression):
            return True

        return self.to_dict() != other.to_dict()
