#!/usr/bin/env python3

import signal
from time import sleep
from helpers import get_logger, set_handlers, is_terminate, get_message as __, LOG_FORMAT

# A simple process that prints the log to standard output.

if __name__ == '__main__':
    logger = get_logger('logging_graylog', LOG_FORMAT)
    set_handlers([signal.SIGTERM, signal.SIGINT])
    while True:
        logger.info(__('process started'))
        for i in range(100):
            if is_terminate():
                break
            if not (i + 1) % 10:
                record = {
                    "label": "test%s" % (i + 1),
                    "counter": i + 1
                 }
                logger.info(__('process executing', report=record))
            sleep(1)
        logger.info(__('process stopped'))
        if is_terminate():
            break
