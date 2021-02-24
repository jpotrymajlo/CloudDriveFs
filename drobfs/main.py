#!/usr/bin/env python2

import logging
import os
from drobfs.auth.dropbox import DropboxAuth
import sys


import argparse
import asyncio
import stat
import errno
import drobfs.handlers

try:
    import faulthandler
except ImportError:
    pass
else:
    faulthandler.enable()

#pyfuse2_asyncio.enable()
logger = logging.getLogger('drobfs')


def parse_args():
    '''Parse command line'''

    parser = argparse.ArgumentParser()

    parser.add_argument('mountpoint', type=str,
                        help='Where to mount the file system')
    parser.add_argument('--debug', action='store_true', default=False,
                        help='Enable debugging output')
    parser.add_argument('--debug-fuse', action='store_true', default=False,
                        help='Enable FUSE debugging output')
    return parser.parse_args()


def main():
#    options = parse_args()

    logger.setLevel(logging.DEBUG)

    
    sh = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s [%(name)s %(levelname)s] %(message)s')
    sh.setFormatter(formatter)
    logger.addHandler(sh)
    
    logger.debug('+++ start Dropbox')
    dropbox = DropboxAuth("file")
    dropbox.get_token()
    logger.debug('--- start Dropbox')

 #   access_token = new auth.AccessToken(81a3hh7rvxf40po, 82a3hh7rvxf40po )
#    token = access_token.get_token()


#    testfs = handlers.FuseHandlers()
#    fuse_options = set(pyfuse2.default_options)
#    fuse_options.add('fsname=CloudFs')
#    if options.debug_fuse:
#        fuse_options.add('debug')
#
#    logger.info("start fs")
##
#    pyfuse2.init(testfs, "/media/jacek/cloudfs", fuse_options)
#    loop = asyncio.get_event_loop()
#    try:
#        loop.run_until_complete(pyfuse2.main())
#    except:
#        pyfuse2.close(unmount=False)
#        raise
#    finally:
#        loop.close()

#    pyfuse2.close()

