#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test Interwiki Graph functionality."""
#
# (C) Pywikibot team, 2015-2020
#
# Distributed under the terms of the MIT license.
#
from __future__ import absolute_import, division, unicode_literals

from pywikibot import interwiki_graph

from tests.aspects import unittest, require_modules, SiteAttributeTestCase
from tests.utils import DryPage


@require_modules('pydot')
class TestWiktionaryGraph(SiteAttributeTestCase):

    """Tests for interwiki links to local sites."""

    sites = {
        'enwikt': {
            'family': 'wiktionary',
            'code': 'en',
        },
        'frwikt': {
            'family': 'wiktionary',
            'code': 'fr',
        },
        'plwikt': {
            'family': 'wiktionary',
            'code': 'pl',
        },
    }
    dry = True

    @classmethod
    def setUpClass(cls):
        """Setup test class."""
        super(TestWiktionaryGraph, cls).setUpClass()

        cls.pages = {
            'en': DryPage(cls.enwikt, 'origin'),
            'en2': DryPage(cls.enwikt, 'origin2'),
            'fr': DryPage(cls.frwikt, 'origin'),
            'pl': DryPage(cls.plwikt, 'origin'),
        }

    def setUp(self):
        """Setup interwiki_graph data."""
        super(TestWiktionaryGraph, self).setUp()
        data = interwiki_graph.Subject(self.pages['en'])
        data.found_in[self.pages['en']] = [self.pages['fr'], self.pages['pl']]
        data.found_in[self.pages['fr']] = [self.pages['en'], self.pages['pl']]
        data.found_in[self.pages['pl']] = [self.pages['en'], self.pages['fr']]
        self.data = data

    def test_simple_graph(self):
        """Test that GraphDrawer.createGraph does not raise exception."""
        drawer = interwiki_graph.GraphDrawer(self.data)
        drawer.createGraph()

    def test_octagon(self):
        """Test octagon nodes."""
        self.data.found_in[self.pages['en2']] = [self.pages['fr']]
        drawer = interwiki_graph.GraphDrawer(self.data)

        self.assertEqual({self.pages['en'].site}, drawer._octagon_site_set())

        drawer.createGraph()
        nodes = drawer.graph.obj_dict['nodes']

        for node, shape in [('"pl:origin"', 'rectangle'),
                            ('"fr:origin"', 'rectangle'),
                            ('"en:origin"', 'octagon')]:
            with self.subTest(node=node):
                self.assertEqual(
                    nodes[node][0]['attributes']['shape'], shape)


if __name__ == '__main__':  # pragma: no cover
    try:
        unittest.main()
    except SystemExit:
        pass
