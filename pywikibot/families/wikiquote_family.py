# -*- coding: utf-8 -*-
"""Family module for Wikiquote."""
#
# (C) Pywikibot team, 2005-2020
#
# Distributed under the terms of the MIT license.
#
from pywikibot import family


# The Wikimedia family that is known as Wikiquote
class Family(family.SubdomainFamily, family.WikimediaFamily):

    """Family class for Wikiquote."""

    name = 'wikiquote'

    closed_wikis = [
        # See https://noc.wikimedia.org/conf/highlight.php?file=dblists/closed.dblist  # noqa
        'als', 'am', 'ang', 'ast', 'bm', 'co', 'cr', 'ga', 'kk',
        'kr', 'ks', 'kw', 'lb', 'na', 'nds', 'qu', 'simple',
        'tk', 'tt', 'ug', 'vo', 'za', 'zh-min-nan',
    ]

    removed_wikis = [
        # See https://noc.wikimedia.org/conf/highlight.php?file=dblists/deleted.dblist  # noqa
        'tokipona',
    ]

    languages_by_size = [
        'en', 'it', 'pl', 'ru', 'cs', 'fa', 'de', 'pt', 'es', 'fr', 'uk', 'he',
        'sk', 'bs', 'tr', 'ca', 'fi', 'sl', 'az', 'lt', 'eo', 'zh', 'bg', 'hr',
        'hy', 'el', 'ar', 'su', 'id', 'nn', 'et', 'sv', 'li', 'hu', 'ko', 'nl',
        'ja', 'la', 'ta', 'th', 'sah', 'sr', 'gu', 'gl', 'ur', 'te', 'be',
        'cy', 'no', 'ml', 'sq', 'kn', 'ro', 'ku', 'eu', 'uz', 'hi', 'ka', 'da',
        'sa', 'is', 'vi', 'br', 'mr', 'af', 'wo', 'ky',
    ]

    category_redirect_templates = {
        '_default': (),
        'ar': ('قالب:تحويل تصنيف',),
        'en': ('Category redirect',),
        'ro': ('Redirect categorie',),
        'sq': ('Kategori e zhvendosur',),
        'uk': ('Categoryredirect',),
    }

    # Global bot allowed languages on
    # https://meta.wikimedia.org/wiki/BPI#Current_implementation
    # & https://meta.wikimedia.org/wiki/Special:WikiSets/2
    cross_allowed = [
        'af', 'ar', 'az', 'be', 'bg', 'br', 'bs', 'ca', 'cs',
        'cy', 'da', 'el', 'eo', 'es', 'et', 'eu', 'fa', 'fi',
        'fr', 'gl', 'gu', 'he', 'hi', 'hu', 'hy', 'id', 'is',
        'it', 'ja', 'ka', 'kn', 'ko', 'ku', 'ky', 'la', 'li',
        'lt', 'ml', 'mr', 'nl', 'nn', 'no', 'pt', 'ro', 'ru',
        'sa', 'sah', 'sk', 'sl', 'sq', 'sr', 'su', 'sv', 'ta',
        'te', 'th', 'tr', 'uk', 'ur', 'uz', 'vi', 'wo', 'zh',
    ]

    # Subpages for documentation.
    # TODO: List is incomplete, to be completed for missing languages.
    doc_subpages = {
        '_default': (('/doc', ),
                     ['en']
                     ),
        'sr': ('/док', ),
    }

    def encodings(self, code):
        """
        Return a list of historical encodings for a specific language.

        @param code: site code
        """
        # Historic compatibility
        if code == 'pl':
            return 'utf-8', 'iso8859-2'
        if code == 'ru':
            return 'utf-8', 'iso8859-5'
        return super().encodings(code)
