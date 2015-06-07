"""
awslimitchecker/services/base.py

The latest version of this package is available at:
<https://github.com/jantman/awslimitchecker>

################################################################################
Copyright 2015 Jason Antman <jason@jasonantman.com> <http://www.jasonantman.com>

    This file is part of awslimitchecker, also known as awslimitchecker.

    awslimitchecker is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    awslimitchecker is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with awslimitchecker.  If not, see <http://www.gnu.org/licenses/>.

The Copyright and Authors attributions contained herein may not be removed or
otherwise altered, except to add the Author attribution of a contributor to
this work. (Additional Terms pursuant to Section 7b of the AGPL v3)
################################################################################
While not legally required, I sincerely request that anyone who finds
bugs please submit them at <https://github.com/jantman/pydnstest> or
to me via email, and that you send any contributions or improvements
either as a pull request on GitHub, or to me via email.
################################################################################

AUTHORS:
Jason Antman <jason@jasonantman.com> <http://www.jasonantman.com>
################################################################################
"""

import abc
import logging
logger = logging.getLogger(__name__)


class AwsService(object):
    __metaclass__ = abc.ABCMeta

    service_name = 'baseclass'

    def __init__(self):
        """
        Describes an AWS service and its limits, and provides methods to
        query current utilization.

        Constructors of AwsService subclasses *must not* make any external
        connections; these must be made lazily as needed in other methods.
        AwsService subclasses should be usable without any external network
        connections.
        """
        self.limits = None
        self.limits = self.get_limits()
        self.conn = None

    @abc.abstractmethod
    def check_usage(self):
        """
        Check this service for the usage of each resource with a known limit.

        :returns: dict of limit name (string) to usage amount
        :rtype: dict
        """
        raise NotImplementedError('abstract base class')

    @abc.abstractmethod
    def get_limits(self):
        """
        Return all known limits for this service, as a dict of their names
        to :py:class:`~.AwsLimit` objects.

        :returns: dict of limit names to :py:class:`~.AwsLimit` objects
        :rtype: dict
        """
        raise NotImplementedError('abstract base class')