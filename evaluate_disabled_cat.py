#!/usr/bin/python
# -*- coding: utf-8  -*-
"""
This module offers a wide variety of page generators. A page generator is an
object that is iterable (see http://www.python.org/dev/peps/pep-0255/ ) and
that yields page objects on which other scripts can then work.

In general, there is no need to run this script directly. It can, however,
be run for testing purposes. It will then print the page titles to standard
output.

These parameters are supported to specify which pages titles to print:

python evaluate_diabled_cat.py -search=':AfC submissions with missing AfC template' -ns:5
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



# if a bot uses GeneratorFactory, the module should include the line
#   docuReplacements = {'&params;': pywikibot.pagegenerators.parameterHelp}
# and include the marker &params; in the module's docstring

def main(*args):
    try:
        genFactory = pagegenerators.GeneratorFactory()
        for arg in pywikibot.handleArgs(*args):
            if not genFactory.handleArg(arg):
                pywikibot.showHelp()
                break
        else:
            gen = genFactory.getCombinedGenerator()
            if gen:
              page_match = re.compile('\{\{AFC submission\|')
              summary = u"[[User:HasteurBot|HasteurBot Task 3]]: Removing " + \
                u"maint category that does not apply"
              disclude_list = [
                u'Wikipedia talk:WikiProject Articles for creation',
                u'Wikipedia talk:WikiProject Articles for creation/2013 5',
                u'Wikipedia talk:WikiProject Articles for creation/2011',
              ]
              for article in gen:
                if article.title() in disclude_list:
                  continue
                art_text = article.get()
                if page_match.match(art_text) is not None:
                  print article 
                  art_1 = re.sub(
                    '\\\n\[\[\:Category\:AfC_submissions_with_missing_AfC_template\]\]',
                    '',
                    art_text
                  )
                  art_2 = re.sub(
                    '\\\n\[\[\:Category\:AfC submissions with missing AfC template\]\]',
                    '',
                    art_1
                  )
                  #article.put(art_2,comment=summary)
            else:
                pywikibot.showHelp()
    finally:
        pywikibot.stopme()


if __name__=="__main__":
    main()
