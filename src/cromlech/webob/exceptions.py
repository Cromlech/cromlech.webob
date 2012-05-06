# -*- coding: utf-8 -*-

import grokcore.component as grok
from cromlech.browser import IRequest, IResponse, IResponseFactory
from cromlech.browser import IHTTPRedirect, redirect_exception_response
from cromlech.webob.response import Response


@grok.adapter(IRequest, IHTTPRedirect)
@grok.implementer(IResponse)
def exception_response(request, exception):
    return redirect_exception_response(Response, exception)


@grok.adapter(IRequest, IHTTPRedirect)
@grok.implementer(IResponseFactory)
def exception_response_factory(request, exception):
    def make_exception_response():
        return redirect_exception_response(Response, exception)
    return make_exception_response
