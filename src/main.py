import logging
import handlers
import argparse
import pyfuse3
import pyfuse3_asyncio
import asyncio

logger = logging.getLogger(__name__)

def parse_cmdline():
    parser = argparse.ArgumentParser()
    parser.add_argument("mountpoint", type=str, help="mounting point for filesystems")
    return parser.parse_args()

def main():
    pyfuse3_asyncio.enable()

    options = parse_cmdline()

    logger.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s [%(name)s %(levelname)s] %(message)s')
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    logger.info("start CloudDriveFs")

    fuseHandlers = handlers.FuseHandlers()

    fuseOptions = set(pyfuse3.default_options)
    fuseOptions.add("fsname=DropboxFs")

    pyfuse3.init(fuseHandlers, "/media/jacek/cloudfs", fuseOptions)

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