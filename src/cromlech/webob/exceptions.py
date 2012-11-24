# -*- coding: utf-8 -*-

import crom

from .response import Response
from cromlech.browser import IRequest, IResponse, IResponseFactory
from cromlech.browser import IHTTPRedirect, redirect_exception_response


@crom.adapter
@crom.sources(IRequest, IHTTPRedirect)
@crom.target(IResponse)
def exception_response(request, exception):
    return redirect_exception_response(Response, exception)


@crom.adapter
@crom.sources(IRequest, IHTTPRedirect)
@crom.target(IResponseFactory)
def exception_response_factory(request, exception):
    def make_exception_response():
        return redirect_exception_response(Response, exception)
    return make_exception_response
