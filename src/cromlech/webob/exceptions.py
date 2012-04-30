# -*- coding: utf-8 -*-

import grokcore.component as grok
from cromlech.browser import IRequest, IResponse
from cromlech.browser import IHTTPRedirect, redirect_exception_response
from cromlech.webob.response import Response


@grok.adapter(IRequest, IHTTPRedirect)
@grok.implementer(IResponse)
def exception_view(request, exception):
    return redirect_exception_response(Response, exception)
