import sys
import multiprocessing

from botutils import streamer
from botutils import utils
from botutils import follower
from botutils import config

logger = utils.get_logger()

if __name__ == '__main__':
    logger.info('Starting Twitter Bot')
    api = config.get_api()
    p1 = multiprocessing.Process(target=streamer.run_streamer, args=(api, 'follow',))
    p2 = multiprocessing.Process(target=follower.follower_bot, args=(api,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    #streamer.run_streamer(mode='follow')
    