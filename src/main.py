#!/usr/bin/env python3

import os
import sys


import argparse
import asyncio
import stat
import logging
import errno
import pyfuse3
import pyfuse3_asyncio
import handlers

try:
    import faulthandler
except ImportError:
    pass
else:
    faulthandler.enable()

pyfuse3_asyncio.enable()
logger = logging.getLogger(__name__)

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
    options = parse_args()

    logger.setLevel(logging.DEBUG)
    
    sh = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s [%(name)s %(levelname)s] %(message)s')
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    testfs = handlers.FuseHandlers()
    fuse_options = set(pyfuse3.default_options)
    fuse_options.add('fsname=CloudFs')
    if options.debug_fuse:
        fuse_options.add('debug')

    logger.info("start fs")

    pyfuse3.init(testfs, "/media/jacek/cloudfs", fuse_options)
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(pyfuse3.main())
    except:
        pyfuse3.close(unmount=False)
        raise
    finally:
        loop.close()

    pyfuse3.close()


if __name__ == '__main__':
    main()
