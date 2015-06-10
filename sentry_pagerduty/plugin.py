# Copyright 2015 Depop Ltd

import sentry_pagerduty
import pygerduty
from sentry_pagerduty.forms import PagerDutyConfigForm
from sentry.plugins import Plugin


class PagerDutyPlugin(Plugin):
    """
    Sentry plugin to send errors stats to Pagerduty.
    """
    author = 'Depop developers'
    author_url = 'https://github.com/depop/sentry-pagerduty'
    version = sentry_pagerduty.VERSION
    description = 'Send error occurence to Pagerduty.'
    slug = 'pagerduty'
    title = 'Pagerduty'
    conf_key = slug
    conf_title = title
    resource_links = [
        ('Source', 'https://github.com/depop/sentry-pagerduty'),
        ('Bug Tracker', 'https://github.com/depop/sentry-pagerduty/issues'),
        ('README', 'https://github.com/depop/sentry-pagerduty/blob/master/README.rst'),
    ]
    project_conf_form = PagerDutyConfigForm

    def is_configured(self, project, **kwargs):
        params = self.get_option
        return (params('api_key', project) and
                params('service_key', project) and
                params('domain_name', project))

    def post_process(self, group, event, is_new, is_sample, **kwargs):
        if not self.is_configured(group.project):
            return

        api_key = self.get_option('api_key', group.project)
        domain_name = self.get_option('domain_name', group.project)
        service_key = self.get_option('service_key', group.project)

        client = pygerduty.PagerDuty(domain_name, api_key)
        client.trigger_incident(service_key, event.message)
