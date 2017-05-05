#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""A script to process items from a redis queue."""
from __future__ import print_function, unicode_literals

import argparse
import json
import logging
import pprint
import sys
import time
from redis import StrictRedis

from scrapy_redis import get_redis


logger = logging.getLogger('process_items')


def process_items(r, keys, timeout, limit=0, log_every=10, wait=.1):
    """Process items from a redis queue.

    Parameters
    ----------
    r : Redis
        Redis connection instance.
    keys : list
        List of keys to read the items from.
    timeout: int
        Read timeout.

    """
    limit = limit or float('inf')
    processed = 0
    while processed < limit:
        # Change ``blpop`` to ``brpop`` to process as LIFO.
        ret = r.blpop(keys, timeout)
        # If data is found before the timeout then we consider we are done.
        if ret is None:
            time.sleep(wait)
            continue

        source, data = ret
        try:
            item = json.loads(data)
        except Exception:
            logger.exception("Failed to load item:\n%r", pprint.pformat(data))
            continue

        try:
            logger.info(str(item))
            with open('a.txt', 'a') as f:
                f.write(str(item) + '\n')
        except Exception:
            logger.error('failed')
            continue

        processed += 1
        if processed % log_every == 0:
            logger.info("Processed %s items", processed)


def main():
    params = {}
    params['password'] = 'mima'
    params['host'] = '123.207.253.201'
    r = StrictRedis(**params)
    host = r.connection_pool.get_connection('info').host
    logger.info("Waiting for items in '%s' (server: %s)", 'moko_spider:items', host)
    kwargs = {
        'keys': ['moko_spider:items'],
        'timeout': 0,
        'limit': 0,
        # 'log_every': args.progress_every,
    }
    try:
        process_items(r, **kwargs)
        retcode = 0  # ok
    except KeyboardInterrupt:
        retcode = 0  # ok
    except Exception:
        logger.exception("Unhandled exception")
        retcode = 2

    return retcode


if __name__ == '__main__':
    sys.exit(main())
