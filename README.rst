sentry-pagerduty
================

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

Time out issues
---------------

You might experience issues with raven client's default timeout beeing to short for pagerduty to respond in time. In that case you need to adjust the timeout accordingly.
Clients that are known to support setting the timeout via the Sentry DSN:

 * Python: http://raven.readthedocs.org/en/latest/transports/index.html?highlight=timeout
 * Java: https://github.com/getsentry/raven-java#timeout-advanced
