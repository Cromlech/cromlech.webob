"""If zope.i18n is present this package will provides adapters of request to
:py:class:`zope.i18n.interfaces.IUserPreferredLanguages`
and :py:class:`zope.i18n.interfaces.locales.ILocale`
"""

from grokcore.component import context, Adapter, adapter, implementer
from zope.i18n.interfaces import IUserPreferredLanguages
from zope.i18n.interfaces.locales import ILocale
from zope.i18n.locales import locales
from zope.interface import implements

from cromlech.webob import IWebObRequest


class RequestPreferredLanguages(Adapter):
    """Adapts request to IUserPreferredLanguages using its headers
    """

    context(IWebObRequest)
    implements(IUserPreferredLanguages)

    def __init__(self, request):
        self.request = request

    def getPreferredLanguages(self):
        return self.request.accept_language.best_matches()


@adapter(IWebObRequest)
@implementer(ILocale)
def get_locale(request):
    """Adapts request to ILocale based on preferred language.

    hunder the hood a call to IUserPreferredLanguages will help decide
    language.
    """
    langs = IUserPreferredLanguages(request).getPreferredLanguages()
    if not langs or langs[0] == '':
        return locales.getLocale(None, None, None)
    else:
        parts = (langs[0].split('-') + [None, None])[:3]
        return locales.getLocale(*parts)
