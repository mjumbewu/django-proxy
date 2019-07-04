Django HTTP Proxy
=================

**Simple HTTP proxy service as a Django app.**

**Author:** Mjumbe Wawatu Ukweli, [Follow me on Twitter][1].

Installation
============

Install with

```console
$ pip install django-proxy
```

Overview
========

Forward as close to an exact copy of the request as possible along to a
given url.  Respond with as close to an exact copy of the resulting
response as possible.

Includes a view function that can be used directly from a URL spec:

```python
from proxy.views import proxy_view

urlpatterns = patterns(
	...
	url('proxy/(?P<url>.*)', proxy_view),
	...
)
```

Or from another view function:

```python
from django.views.decorators.csrf import csrf_exempt
from proxy.views import proxy_view

@csrf_exempt
def myview(request, path):
	extra_requests_args = {...}
	remoteurl = 'http://<host_name>/' + path
	return proxy_view(request, remoteurl, extra_requests_args)
	
urlpatterns = patterns(
	...
	url('proxy/(?P<path>.*)', myview),
	...
)
```

Changelog
=========

1.2.0
-----
* Convert relative URLs in `Location` headers to absolute.

1.0.2
-----

* Add `Content-length` to the set of headers not copies from the upstream
  response.

1.0.1
-----

* Defer to the `requests` library for setting the Content-Length header

1.0.0
-----

* Initial release, based on the HTTP proxy in OpenPlans'
  https://github.com/openplans/shareabouts-django-client

License
=======

Copyright © Mjumbe Wawatu Ukweli.

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this
list of conditions and the following disclaimer in the documentation and/or
other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

[1]: http://twitter.com/mjumbewu
