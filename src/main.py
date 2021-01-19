import logging
import handlers

logger = logging.getLogger(__name__)

def main():
    logger.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s [%(name)s %(levelname)s] %(message)s')
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    logger.info("start CloudDriveFs")


if __name__ == '__main__':
    main()