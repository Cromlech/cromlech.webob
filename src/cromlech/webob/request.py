# -*- coding: utf-8 -*-

import webob
from UserDict import UserDict
from cromlech.browser.interfaces import IHTTPRequest
from cromlech.webob import IWebObRequest
from grokcore.component import context, Adapter
from zope.cachedescriptors.property import CachedProperty
from zope.interface import implements


class FormParams(UserDict):
    def __init__(self, params):
        self.data = params.mixed()
        self.params = params


class Request(webob.Request):
    implements(IHTTPRequest)

    @property
    def environment(self):
        return self.environ

    @CachedProperty
    def form(self):
        return FormParams(self.params)


Request.RequestClass = Request


class RequestAdapter(Adapter):
    context(IWebObRequest)
    implements(IHTTPRequest)

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
