# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.2885
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


class PolicyResponse(object):
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
        'id': 'PolicyId',
        'description': 'str',
        'applications': 'list[str]',
        'grant': 'Grant',
        'selectors': 'list[SelectorDefinition]',
        '_for': 'list[ForSpec]',
        '_if': 'list[IfExpression]',
        'when': 'WhenSpec',
        'how': 'HowSpec',
        'links': 'list[Link]'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'applications': 'applications',
        'grant': 'grant',
        'selectors': 'selectors',
        '_for': 'for',
        '_if': 'if',
        'when': 'when',
        'how': 'how',
        'links': 'links'
    }

    required_map = {
        'id': 'optional',
        'description': 'optional',
        'applications': 'optional',
        'grant': 'optional',
        'selectors': 'optional',
        '_for': 'optional',
        '_if': 'optional',
        'when': 'optional',
        'how': 'optional',
        'links': 'optional'
    }

    def __init__(self, id=None, description=None, applications=None, grant=None, selectors=None, _for=None, _if=None, when=None, how=None, links=None, local_vars_configuration=None):  # noqa: E501
        """PolicyResponse - a model defined in OpenAPI"
        
        :param id: 
        :type id: finbourne_access.PolicyId
        :param description:  Description of what the policy is entitling
        :type description: str
        :param applications:  Applications to which the policy applies
        :type applications: list[str]
        :param grant: 
        :type grant: finbourne_access.Grant
        :param selectors:  Selectors that this policy will be applied to
        :type selectors: list[finbourne_access.SelectorDefinition]
        :param _for:  \"For Specification\" for when the policy is to be applied
        :type _for: list[finbourne_access.ForSpec]
        :param _if:  \"If Specification\" for when the policy is to be applied
        :type _if: list[finbourne_access.IfExpression]
        :param when: 
        :type when: finbourne_access.WhenSpec
        :param how: 
        :type how: finbourne_access.HowSpec
        :param links: 
        :type links: list[finbourne_access.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._description = None
        self._applications = None
        self._grant = None
        self._selectors = None
        self.__for = None
        self.__if = None
        self._when = None
        self._how = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.description = description
        self.applications = applications
        if grant is not None:
            self.grant = grant
        self.selectors = selectors
        self._for = _for
        self._if = _if
        if when is not None:
            self.when = when
        if how is not None:
            self.how = how
        self.links = links

    @property
    def id(self):
        """Gets the id of this PolicyResponse.  # noqa: E501


        :return: The id of this PolicyResponse.  # noqa: E501
        :rtype: finbourne_access.PolicyId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PolicyResponse.


        :param id: The id of this PolicyResponse.  # noqa: E501
        :type id: finbourne_access.PolicyId
        """

        self._id = id

    @property
    def description(self):
        """Gets the description of this PolicyResponse.  # noqa: E501

        Description of what the policy is entitling  # noqa: E501

        :return: The description of this PolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PolicyResponse.

        Description of what the policy is entitling  # noqa: E501

        :param description: The description of this PolicyResponse.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def applications(self):
        """Gets the applications of this PolicyResponse.  # noqa: E501

        Applications to which the policy applies  # noqa: E501

        :return: The applications of this PolicyResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        """Sets the applications of this PolicyResponse.

        Applications to which the policy applies  # noqa: E501

        :param applications: The applications of this PolicyResponse.  # noqa: E501
        :type applications: list[str]
        """

        self._applications = applications

    @property
    def grant(self):
        """Gets the grant of this PolicyResponse.  # noqa: E501


        :return: The grant of this PolicyResponse.  # noqa: E501
        :rtype: finbourne_access.Grant
        """
        return self._grant

    @grant.setter
    def grant(self, grant):
        """Sets the grant of this PolicyResponse.


        :param grant: The grant of this PolicyResponse.  # noqa: E501
        :type grant: finbourne_access.Grant
        """

        self._grant = grant

    @property
    def selectors(self):
        """Gets the selectors of this PolicyResponse.  # noqa: E501

        Selectors that this policy will be applied to  # noqa: E501

        :return: The selectors of this PolicyResponse.  # noqa: E501
        :rtype: list[finbourne_access.SelectorDefinition]
        """
        return self._selectors

    @selectors.setter
    def selectors(self, selectors):
        """Sets the selectors of this PolicyResponse.

        Selectors that this policy will be applied to  # noqa: E501

        :param selectors: The selectors of this PolicyResponse.  # noqa: E501
        :type selectors: list[finbourne_access.SelectorDefinition]
        """

        self._selectors = selectors

    @property
    def _for(self):
        """Gets the _for of this PolicyResponse.  # noqa: E501

        \"For Specification\" for when the policy is to be applied  # noqa: E501

        :return: The _for of this PolicyResponse.  # noqa: E501
        :rtype: list[finbourne_access.ForSpec]
        """
        return self.__for

    @_for.setter
    def _for(self, _for):
        """Sets the _for of this PolicyResponse.

        \"For Specification\" for when the policy is to be applied  # noqa: E501

        :param _for: The _for of this PolicyResponse.  # noqa: E501
        :type _for: list[finbourne_access.ForSpec]
        """

        self.__for = _for

    @property
    def _if(self):
        """Gets the _if of this PolicyResponse.  # noqa: E501

        \"If Specification\" for when the policy is to be applied  # noqa: E501

        :return: The _if of this PolicyResponse.  # noqa: E501
        :rtype: list[finbourne_access.IfExpression]
        """
        return self.__if

    @_if.setter
    def _if(self, _if):
        """Sets the _if of this PolicyResponse.

        \"If Specification\" for when the policy is to be applied  # noqa: E501

        :param _if: The _if of this PolicyResponse.  # noqa: E501
        :type _if: list[finbourne_access.IfExpression]
        """

        self.__if = _if

    @property
    def when(self):
        """Gets the when of this PolicyResponse.  # noqa: E501


        :return: The when of this PolicyResponse.  # noqa: E501
        :rtype: finbourne_access.WhenSpec
        """
        return self._when

    @when.setter
    def when(self, when):
        """Sets the when of this PolicyResponse.


        :param when: The when of this PolicyResponse.  # noqa: E501
        :type when: finbourne_access.WhenSpec
        """

        self._when = when

    @property
    def how(self):
        """Gets the how of this PolicyResponse.  # noqa: E501


        :return: The how of this PolicyResponse.  # noqa: E501
        :rtype: finbourne_access.HowSpec
        """
        return self._how

    @how.setter
    def how(self, how):
        """Sets the how of this PolicyResponse.


        :param how: The how of this PolicyResponse.  # noqa: E501
        :type how: finbourne_access.HowSpec
        """

        self._how = how

    @property
    def links(self):
        """Gets the links of this PolicyResponse.  # noqa: E501


        :return: The links of this PolicyResponse.  # noqa: E501
        :rtype: list[finbourne_access.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PolicyResponse.


        :param links: The links of this PolicyResponse.  # noqa: E501
        :type links: list[finbourne_access.Link]
        """

        self._links = links

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
        if not isinstance(other, PolicyResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PolicyResponse):
            return True

        return self.to_dict() != other.to_dict()
