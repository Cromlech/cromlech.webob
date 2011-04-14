"""
If zope.i18n is present this package will provides adapters of request to 
:py:class:`zope.i18n.interfaces.IUserPreferredLanguages` 
and :py:class:`zope.i18n.interfaces.locales.ILocale`
"""

from zope.i18n.interfaces import IUserPreferredLanguages
from zope.i18n.interfaces.locales import ILocale
from zope.i18n.locales import locales

from grokcore.components import implements, adapts, adapter, implementer

from cromlech.webob import request

class RequestPreferredLanguages(object):
    """Adapts request to IUserPreferredLanguages using its headers
    """

    adapts(request.Request)
    implements(IUserPreferredLanguages)

    def __init__(self, request):
        self.request = request
        
    def getPreferredLanguages(self):
        return self.request.accept_language.best_matches()

@adapter(request.Request)
@implementer(ILocale)
def get_locale(request):
    """Adapts request to ILocale based on preferred language.
    
    hunder the hood a call to IUserPreferredLanguages will help decide 
    language.
    """
    langs = IUserPreferredLanguages(request)
    if not langs or langs[0] == '':
        return locales.getLocale(None, None, None)
    else:
        parts = (langs[0].split('-') + [None, None])[:3]
        return locales.getLocale(*parts)
