sentry-pagerduty
================

A plugin for sentry that enables sending events on to a PagerDuty instance.

Install
-------

Install the package with ``pip``::

    pip install git+git://github.com/depop/sentry-pagerduty.git


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
This prooves challenging since providing a timeout query with the DSN is currently beeing disabled (https://github.com/getsentry/raven-python/issues/253) as is passing a timeout value 
during client instance creation (https://github.com/getsentry/raven-python/issues/183).

A temporarily solution which does not include changing 3rd party code would be to manually configure the client with a custom transport class e.g.::

    from urlparse import urlparse
    from raven import Client
    from raven.transport.base import HTTPTransport

    # instantiate client as usual
    client = Client('http://<public_key>:<secret_key>@0.0.0.0:9000/2')

    # create transport with custom timeout and register it with your sentry instance 
    transport = HTTPTransport(urlparse("http://0.0.0.0:9000/api/store/"), timeout=30)
    client._registry._transports["http://0.0.0.0:9000/api/store/"] = transport

    # use client at your convenience
    client.captureMessage('hello world')
