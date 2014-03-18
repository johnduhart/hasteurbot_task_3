#!/usr/bin/python
# -*- coding: utf-8  -*-
"""
python add_magic_cat.py
"""
#
# (C) Pywikipedia bot team, 2005-2013
#
# Distributed under the terms of the MIT license.
#
__version__='$Id$'

import re
import sys
import codecs
import datetime
import urllib, urllib2, time
import traceback
import wikipedia as pywikibot
import config
from pywikibot import i18n
from pywikibot.support import deprecate_arg
import date, catlib, userlib, query
import pagegenerators
import pdb

# if a bot uses GeneratorFactory, the module should include the line
#   docuReplacements = {'&params;': pywikibot.pagegenerators.parameterHelp}
# and include the marker &params; in the module's docstring
excluded_list = [
  'Articles_for_creation/2006-01-13',
  'Articles_for_creation/2006-01-16',
  'Articles_for_creation/2006-01-13',
  'Articles_for_creation/2006-02-11',
  'Articles_for_creation/2006-03-10',
  'Articles_for_creation/2006-04-09',
  'Articles_for_creation/2006-04-22',
  'Articles_for_creation/2006-05-01',
  'Articles_for_creation/2006-05-09',
  'Articles_for_creation/2006-05-22',
  'Articles_for_creation/2006-05-25',
  'Articles_for_creation/2006-06-07',
  'Articles_for_creation/2006-07-29',
  'Articles_for_creation/2006-07-30',
  'Articles_for_creation/2006-08-02',
  'Articles_for_creation/2006-08-20',
  'Articles_for_creation/2006-11-07',
  'Articles_for_creation/2006-11-15',
  'Articles_for_creation/2006-11-17',
  'Articles_for_creation/2006-11-20',
  'Articles_for_creation/2006-12-19',
  'Articles_for_creation/2006-12-25',
  'Articles_for_creation/2007-01-22',
  'Articles_for_creation/2007-02-28',
  'Articles_for_creation/2007-03-09',
  'Articles_for_creation/2007-05-11',
  'Articles_for_creation/2007-05-13',
  'Articles_for_creation/2007-06-08',
  'Articles_for_creation/2007-06-26',
  'Articles_for_creation/2007-07-17',
  'Articles_for_creation/2007-07-18',
  'Articles_for_creation/2007-08-09',
  'Articles_for_creation/2007-08-23',
  'Articles_for_creation/2007-08-24',
  'Articles_for_creation/2007-09-06',
  'Articles_for_creation/2007-09-19',
  'Articles_for_creation/2007-09-27',
  'Articles_for_creation/2007-10-10',
  'Articles_for_creation/2007-10-13',
  'Articles_for_creation/2007-10-18',
  'Articles_for_creation/2007-11-06',
  'Articles_for_creation/2007-11-22',
  'Articles_for_creation/2008-02-04',
  'Articles_for_creation/2008-06-05',
  'Articles_for_creation/2008-07-11',
  'Articles_for_creation/2008-07-21',
  ]
def excluded_page(page_title):
    if page_title in excluded_list:
        return True
    return False


def main(*args):
    try:
        list_page = pywikibot.Page(pywikibot.getSite(),
            'User:Petrb/Weird pages'
        )
        page_text = list_page.get()
        lines = page_text.split('\n')
        list_elems = lines[1:-2]
        summary = u"[[User:HasteurBot|HasteurBot Task 5]]: Adding maint " +\
            u"category to identified page"
        page_match = re.compile('\{\{A[Ff]C submission\|')
        cat_match = re.compile('\[\[Category\:AfC submissions with missing AfC template\]\]')
        limiter = 50 - 14
        for elem in list_elems:
            if excluded_page(elem):
                continue
            ind_page = pywikibot.Page(pywikibot.getSite(),
                u'Wikipedia talk:'+elem
            )
            if not ind_page.exists():
                continue
            if ind_page.isRedirectPage():
                ind_page = ind_page.getRedirectTarget()
            if ind_page.namespace() != 5:
                continue
            page_text = ind_page.get()
            if page_match.match(page_text) is None \
                and \
                'AfC_submissions_with_missing_AfC_template' not in page_text \
                and \
                'AfC submissions with missing AfC template' not in page_text:
                limiter = limiter - 1
                print elem
                imp_text = page_text + \
                    '\n[[Category:AfC submissions with missing AfC template]]'
                ind_page.put(imp_text, comment=summary)
            if limiter == 0:
                break

    finally:
        pywikibot.stopme()


if __name__=="__main__":
    main()
