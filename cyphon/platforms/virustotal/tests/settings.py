# -*- coding: utf-8 -*-
# Copyright 2017 Dunbar Security Solutions, Inc.
#
# This file is part of Cyphon Engine.
#
# Cyphon Engine is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# Cyphon Engine is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Cyphon Engine. If not, see <http://www.gnu.org/licenses/>.
"""
Tests the TwitterSearch class.
"""

# standard library
import logging

# third party
from django.conf import settings

# local
from platforms.tests.test_apihandler import settings_exist

VIRUSTOTAL_SETTINGS = settings.VIRUSTOTAL

_LOGGER = logging.getLogger(__name__)


if not settings_exist(VIRUSTOTAL_SETTINGS):
    VIRUSTOTAL_TESTS_ENABLED = False
    _LOGGER.warning('VirusTotal authentication credentials are missing, '
                    'so VirusTotal API tests will be skipped.')
else:
    VIRUSTOTAL_TESTS_ENABLED = True
