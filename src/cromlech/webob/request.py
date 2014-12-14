# -*- coding: utf-8 -*-

import crom
import webob

from cromlech.browser import IRequest
from cromlech.webob import IWebObRequest
from zope.cachedescriptors.property import CachedProperty
from zope.interface import implementer

# py3 compatibility
try:
    from UserDict import UserDict
except ImportError:
    from collections import UserDict
    

class FormParams(UserDict):

    def __init__(self, params):
        self.data = params.mixed()
        self.params = params


@implementer(IRequest)
class Request(webob.Request):

    @property
    def environment(self):
        return self.environ

    @CachedProperty
    def form(self):
        return FormParams(self.params)


Request.RequestClass = Request


@crom.adapter
@crom.sources(IWebObRequest)
@crom.target(IRequest)
@implementer(IRequest)
class WebobRequest(object):

    def __init__(self, request):
        self.request = request
        self.script_name = request.script_name
        self.environment = request.environ
        self.body = request.body
        self.application_url = request.application_url
        self.charset = request.charset
        self.method = request.method
        self.path = request.path

    @CachedProperty
    def form(self):
        return FormParams(self.request.params)
