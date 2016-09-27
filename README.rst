sentry-pagerduty
================

**DEPRECATED:** This project now lives in `sentry-plugins <https://github.com/getsentry/sentry-plugins>`_

A plugin for sentry that enables sending events on to a PagerDuty instance.

Install
-------

Install the package with ``pip``::

    pip install git+git://github.com/getsentry/sentry-pagerduty.git


Configuration
-------------

Go to your project's configuration page (Projects -> [Project]) and click on "Manage Plugins".
Switch on Pagerduty by ticking "Enabled" in the appropriate column. Click "Save Changes".
Then select the "Pagerduty" tab and enter the pagerduty api-key, your sentry service-key and the domain name of your pagerduty instance.

License
-------
Apache License
Version 2.0, January 2004
See the LICENSE in this repo
