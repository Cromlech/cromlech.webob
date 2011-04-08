# -*- coding: utf-8 -*-

import urllib
from zope.location import ILocation
from zope.interface import Interface
from zope.component import getMultiAdapter
from grokcore.component import adapter, implementer
from cromlech.webob import IWebObRequest
from cromlech.io import IPublicationRoot
from cromlech.browser.interfaces import IURLResolver


_safe = '@+'  # Characters that we don't want to have quoted


@adapter(Interface, IWebObRequest)
@implementer(IURLResolver)
def URLResolver(context, request):

    if context is None:
        return request.application_url

    # first try to get the __parent__ of the object, no matter whether
    # it provides ILocation or not. If this fails, look up an ILocation
    # adapter. This will always work, as a general ILocation adapter
    # is registered for interface in zope.location (a LocationProxy)
    # This proxy will return a parent of None, causing this to fail
    # More specific ILocation adapters can be provided however.
    try:
        container = context.__parent__
    except AttributeError:
        # we need to assign to context here so we can get
        # __name__ from it below
        context = ILocation(context)
        container = context.__parent__

    if container is None:
        if IPublicationRoot.providedBy(context):
            return request.application_url
        else:
            raise KeyError(context, '__parent__')

    url = getMultiAdapter((container, request), IURLResolver)

    name = getattr(context, '__name__', None)
    if name is None:
        raise KeyError(context, '__name__')

    if name:
        url += '/' + urllib.quote(name.encode('utf-8'), _safe)

    return url
