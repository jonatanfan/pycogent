#!/usr/bin/env python

from cogent.parse.ct import ct_parser

__author__ = "Shandy Wikman"
__copyright__ = "Copyright 2007, The Cogent Project"
__contributors__ = ["Shandy Wikman"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Shandy Wikman"
__email__ = "ens01svn@cs.umu.se"
__status__ = "Development"

def sfold_parser(lines):
    """Parser for Sfold output"""
    result = ct_parser(lines)
    return result