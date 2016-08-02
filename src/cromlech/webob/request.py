# -*- coding: utf-8 -*-

import webob
from webob.compat import bytes_, url_quote
from UserDict import UserDict
from cromlech.browser import IRequest
from cromlech.webob import IWebObRequest
from grokcore.component import context, Adapter
from zope.cachedescriptors.property import CachedProperty
from zope.interface import implements


PATH_SAFE = '/:@&+$,'


def compute_application_url(request):
    virtual = request.environment.get('HTTP_X_VHM_ROOT')
    script_name = request.script_name
    if virtual is not None:
        script_name = script_name.lstrip(virtual)
    bscript_name = bytes_(script_name, request.url_encoding)
    # FIXME : host can be virtual too.
    return request.host_url + url_quote(bscript_name, PATH_SAFE)


class FormParams(UserDict):

    def __init__(self, params):
        self.data = params.mixed()
        self.params = params


class Request(webob.Request):
    implements(IRequest)

    @property
    def environment(self):
        return self.environ

    @CachedProperty
    def form(self):
        return FormParams(self.params)

    @property
    def application_url(self):
        return compute_application_url(self)


Request.RequestClass = Request


class RequestAdapter(Adapter):
    context(IWebObRequest)
    implements(IRequest)

    def __init__(self, request):
        self.request = request
        self.script_name = request.script_name
        self.environment = request.environ
        self.body = request.body
        self.charset = request.charset
        self.method = request.method
        self.path = request.path
        self.url_encoding = request.url_encoding

    @property
    def application_url(self):
        return compute_application_url(self)
        
    @CachedProperty
    def form(self):
        return FormParams(self.request.params)
