# -*- coding: utf-8 -*-

import webob
from grokcore.component import context, Adapter
from zope.interface import implements
from cromlech.io.interfaces import IRequest
from cromlech.webob import IWebObRequest


class Request(webob.Request):
    implements(IRequest)

    @property
    def environment(self):
        return self.environ

    @property
    def form(self):
        return self.request.params


Request.RequestClass = Request


class RequestAdapter(Adapter):
    context(IWebObRequest)
    implements(IRequest)

    def __init__(self, request):
        self.request = request
        self.script_name = request.script_name
        self.environment = request.environ
        self.body = request.body
        self.application_url = request.application_url
        self.charset = request.charset
        self.method = request.method

    @property
    def form(self):
        return self.request.params
