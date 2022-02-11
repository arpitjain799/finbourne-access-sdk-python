# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1716
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


class SelectorDefinition(object):
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
        'metadata_selector_definition': 'MetadataSelectorDefinition',
        'id_selector_definition': 'IdSelectorDefinition',
        'match_all_selector_definition': 'MatchAllSelectorDefinition',
        'policy_selector_definition': 'PolicySelectorDefinition'
    }

    attribute_map = {
        'metadata_selector_definition': 'metadataSelectorDefinition',
        'id_selector_definition': 'idSelectorDefinition',
        'match_all_selector_definition': 'matchAllSelectorDefinition',
        'policy_selector_definition': 'policySelectorDefinition'
    }

    required_map = {
        'metadata_selector_definition': 'optional',
        'id_selector_definition': 'optional',
        'match_all_selector_definition': 'optional',
        'policy_selector_definition': 'optional'
    }

    def __init__(self, metadata_selector_definition=None, id_selector_definition=None, match_all_selector_definition=None, policy_selector_definition=None, local_vars_configuration=None):  # noqa: E501
        """SelectorDefinition - a model defined in OpenAPI"
        
        :param metadata_selector_definition: 
        :type metadata_selector_definition: finbourne_access.MetadataSelectorDefinition
        :param id_selector_definition: 
        :type id_selector_definition: finbourne_access.IdSelectorDefinition
        :param match_all_selector_definition: 
        :type match_all_selector_definition: finbourne_access.MatchAllSelectorDefinition
        :param policy_selector_definition: 
        :type policy_selector_definition: finbourne_access.PolicySelectorDefinition

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._metadata_selector_definition = None
        self._id_selector_definition = None
        self._match_all_selector_definition = None
        self._policy_selector_definition = None
        self.discriminator = None

        if metadata_selector_definition is not None:
            self.metadata_selector_definition = metadata_selector_definition
        if id_selector_definition is not None:
            self.id_selector_definition = id_selector_definition
        if match_all_selector_definition is not None:
            self.match_all_selector_definition = match_all_selector_definition
        if policy_selector_definition is not None:
            self.policy_selector_definition = policy_selector_definition

    @property
    def metadata_selector_definition(self):
        """Gets the metadata_selector_definition of this SelectorDefinition.  # noqa: E501


        :return: The metadata_selector_definition of this SelectorDefinition.  # noqa: E501
        :rtype: finbourne_access.MetadataSelectorDefinition
        """
        return self._metadata_selector_definition

    @metadata_selector_definition.setter
    def metadata_selector_definition(self, metadata_selector_definition):
        """Sets the metadata_selector_definition of this SelectorDefinition.


        :param metadata_selector_definition: The metadata_selector_definition of this SelectorDefinition.  # noqa: E501
        :type metadata_selector_definition: finbourne_access.MetadataSelectorDefinition
        """

        self._metadata_selector_definition = metadata_selector_definition

    @property
    def id_selector_definition(self):
        """Gets the id_selector_definition of this SelectorDefinition.  # noqa: E501


        :return: The id_selector_definition of this SelectorDefinition.  # noqa: E501
        :rtype: finbourne_access.IdSelectorDefinition
        """
        return self._id_selector_definition

    @id_selector_definition.setter
    def id_selector_definition(self, id_selector_definition):
        """Sets the id_selector_definition of this SelectorDefinition.


        :param id_selector_definition: The id_selector_definition of this SelectorDefinition.  # noqa: E501
        :type id_selector_definition: finbourne_access.IdSelectorDefinition
        """

        self._id_selector_definition = id_selector_definition

    @property
    def match_all_selector_definition(self):
        """Gets the match_all_selector_definition of this SelectorDefinition.  # noqa: E501


        :return: The match_all_selector_definition of this SelectorDefinition.  # noqa: E501
        :rtype: finbourne_access.MatchAllSelectorDefinition
        """
        return self._match_all_selector_definition

    @match_all_selector_definition.setter
    def match_all_selector_definition(self, match_all_selector_definition):
        """Sets the match_all_selector_definition of this SelectorDefinition.


        :param match_all_selector_definition: The match_all_selector_definition of this SelectorDefinition.  # noqa: E501
        :type match_all_selector_definition: finbourne_access.MatchAllSelectorDefinition
        """

        self._match_all_selector_definition = match_all_selector_definition

    @property
    def policy_selector_definition(self):
        """Gets the policy_selector_definition of this SelectorDefinition.  # noqa: E501


        :return: The policy_selector_definition of this SelectorDefinition.  # noqa: E501
        :rtype: finbourne_access.PolicySelectorDefinition
        """
        return self._policy_selector_definition

    @policy_selector_definition.setter
    def policy_selector_definition(self, policy_selector_definition):
        """Sets the policy_selector_definition of this SelectorDefinition.


        :param policy_selector_definition: The policy_selector_definition of this SelectorDefinition.  # noqa: E501
        :type policy_selector_definition: finbourne_access.PolicySelectorDefinition
        """

        self._policy_selector_definition = policy_selector_definition

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
        if not isinstance(other, SelectorDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SelectorDefinition):
            return True

        return self.to_dict() != other.to_dict()
