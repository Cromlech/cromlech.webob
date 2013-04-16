# -*- coding: utf-8 -*-

import crom
import webob

from cromlech.browser import IResponse, IWSGIComponent
from cromlech.webob import IWebObResponse
from zope.interface import implements, implementer


class Response(webob.Response):
    implements(IResponse)

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


@crom.adapter
@crom.sources(IWebObResponse)
@crom.target(IResponse)
@implementer(IResponse, IWSGIComponent)
class WebobResponseAdapter(object):

    def __init__(self, wrapped):
        self.context = wrapped

    def __getattr__(self, name):
        if name in IResponse:
            return getattr(self.context, name)
        raise AttributeError(name)

    @apply
    def body():
        def setBody(self, value):
            self.context.write(value)

        def getBody(self):
            return webob.Response.body.fget(self.response)

        return property(getBody, setBody)

    def __str__(self):
        return self.context.body

    def __call__(self, environ, start_response):
        return self.context(environ, start_response)


@crom.adapter
@crom.sources(IWebObResponse)
@crom.target(IWSGIComponent)
@implementer(IWSGIComponent)
class ResponseWSGIAdapter(object):

    def __init__(self, wrapped):
        self.context = wrapped

    def __call__(self, environ, start_response):
        return self.context(environ, start_response)
