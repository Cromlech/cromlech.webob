cromlech.webob
**************

  >>> import grokcore.component
  >>> grokcore.component.testing.grok('cromlech.webob')


Test environnment
=================

  >>> import cromlech.webob
  >>> from cromlech.io.interfaces import IRequest, IResponse
  >>> from zope.interface.verify import verifyClass, verifyObject


Basic verifications
===================

  >>> verifyClass(IRequest, cromlech.webob.request.Request)
  True

  >>> verifyClass(IResponse, cromlech.webob.response.Response)
  True


Adapters
========

  >>> import webob
  >>> request = webob.Request.blank('/path/to/app')
  >>> response = webob.Response()

  >>> adapted_request = IRequest(request)
  >>> adapted_response = IResponse(response)

  >>> verifyObject(IRequest, adapted_request)
  True

  >>> verifyObject(IResponse, adapted_response)
  True


URL
===

Scenario
--------

For a simple scenario : /obj:grandfather/obj:father/obj:me

  >>> from zope.location import Location
  >>> grandfather = Location()
  >>> father = Location()
  >>> me = Location()

  >>> me.__parent__ = father
  >>> me.__name__ = 'Grok'

  >>> father.__parent__ = grandfather
  >>> father.__name__ = 'Krao'

  >>> grandfather.__name__ = 'Ghran'


Without clear publication root
------------------------------

  >>> from zope.component import getMultiAdapter
  >>> from cromlech.browser.interfaces import IURLResolver
  >>> print getMultiAdapter((me, request), IURLResolver)
  Traceback (most recent call last):
  ...
  KeyError: (<zope.location.location.Location object at ...>, '__parent__')


With a defined publication root
-------------------------------

  >>> from cromlech.io import IPublicationRoot
  >>> from zope.interface import directlyProvides
  >>> directlyProvides(grandfather, IPublicationRoot)
  >>> print getMultiAdapter((me, request), IURLResolver)
  http://localhost/Krao/Grok
