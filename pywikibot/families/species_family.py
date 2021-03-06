# -*- coding: utf-8 -*-
"""Family module for Wikimedia species wiki."""
#
# (C) Pywikibot team, 2007-2020
#
# Distributed under the terms of the MIT license.
#
from pywikibot import family


# The wikispecies family
class Family(family.WikimediaOrgFamily):

    """Family class for Wikimedia species wiki."""

    name = 'species'

    interwiki_forward = 'wikipedia'
