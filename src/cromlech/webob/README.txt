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


i18n
=====

We provide adapters to retrieve Locale::

  >>> from zope.i18n.interfaces.locales import ILocale

  >>> locale = ILocale(request)
  >>> locale
  <zope.i18n.locales.Locale object at 0x...>
  >>> locale.getLocaleID()
  ''
  
  >>> request.headers['Accept-Language'] = "fr-fr,fr-be,en"
  >>> ILocale(request).getLocaleID()
  u'fr_FR'


Under the hood locale is choosen thanks to Preffered Language adapter::

  >>> from zope.i18n.interfaces import IUserPreferredLanguages
  >>> preferredLanguages = IUserPreferredLanguages(request)
  >>> preferredLanguages
  <cromlech.webob.i18n.RequestPreferredLanguages object at 0x...>
  >>> preferredLanguages.getPreferredLanguages()
  ['fr-fr', 'fr-be', 'en']
