# -*- coding: utf-8 -*-

import webob
import grokcore.component as grok
from cromlech.browser.interfaces import IHTTPResponse
from cromlech.webob import IWebObResponse


class Response(webob.Response):
    grok.implements(IHTTPResponse)

    @apply
    def body():
        def setBody(self, value):
            if isinstance(value, unicode):
                webob.Response.unicode_body.fset(self, value)
            else:
                webob.Response.body.fset(self, value)

        def getBody(self):
            return webob.Response.body.fget(self)

        return property(getBody, setBody)

    def redirect(self, url, status=302, trusted=False):
        """Sets the response for a redirect.
        """
        self.location = url
        self.status = status

    def __str__(self):
        return self.body


class ResponseAdapter(grok.Adapter):
    grok.context(IWebObResponse)
    grok.implements(IHTTPResponse)

    def __init__(self, response):
        self.response = response

    def __call__(self, *args, **kwargs):
        return self.response(*args, **kwargs)

    def __getattr__(self, name):
        return getattr(self.response, name)

    @apply
    def body():
        def setBody(self, value):
            self.response.write(value)

        def getBody(self):
            return webob.Response.body.fget(self.response)

        return property(getBody, setBody)

    def __str__(self):
        return self.response.body
