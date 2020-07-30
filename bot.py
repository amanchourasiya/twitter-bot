from botutils import streamer
from botutils import utils

logger = utils.get_logger()

if __name__ == '__main__':
    logger.info('Starting Twitter Bot')
    streamer.run_streamer(mode='follow')
    