# Copyright 2015 Depop Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# coding: utf-8
"""
sentry_statsd.forms
"""
from django import forms


class PagerDutyConfigForm(forms.Form):
    api_key = forms.CharField(
        max_length=255,
        help_text='PagerDuty API KEY'
    )

    service_key = forms.CharField(
        max_length=32,
        help_text="PagerDuty's Sentry service Integration Key"
    )

    domain_name = forms.CharField(
        max_length=255,
        help_text="Domain Name of your PagerDuty instance (e.g. 'sterling-cooper')"
    )
