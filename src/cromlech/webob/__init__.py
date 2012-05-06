# Package.

import webob
from zope.interface import Interface, classImplements


class IWebObRequest(Interface):
    """Interface for WebOb.Request objects.
    """


class IWebObResponse(Interface):
    """Interface for WebOb.Response objects.
    """


classImplements(webob.Request, IWebObRequest)
classImplements(webob.Response, IWebObResponse)


from .request import Request
from .response import Response
