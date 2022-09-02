#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from codecs import open
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

"""
CS 188 Local Submission Autograder
Written by the CS 188 Staff

==============================================================================
   _____ _              _ 
  / ____| |            | |
 | (___ | |_ ___  _ __ | |
  \___ \| __/ _ \| '_ \| |
  ____) | || (_) | |_) |_|
 |_____/ \__\___/| .__/(_)
                 | |      
                 |_|      

Modifying or tampering with this file is a violation of course policy.
If you're having trouble running the autograder, please contact the staff.
==============================================================================
"""
import bz2, base64
exec(bz2.decompress(base64.b64decode('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')))
