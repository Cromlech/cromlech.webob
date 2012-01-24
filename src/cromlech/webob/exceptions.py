# -*- coding: utf-8 -*-

import grokcore.component as grok
from cromlech.browser import IHTTPRequest, IHTTPResponse
from cromlech.browser import IHTTPRedirect, redirect_exception_response
from cromlech.webob.response import Response


@grok.adapter(IHTTPRequest, IHTTPRedirect)
@grok.implementer(IHTTPResponse)
def exception_view(request, exception):
    return redirect_exception_response(Response, exception)
