# -*- coding: utf-8 -*-

import datetime
import os
import re
import socket
import sys
import time

def get_datetime_from_epoch(epoch):
    """
    Get datetime from epoch.

    :param epoch: epoch
    :return: datetime formatted string
    """
    fmt = "%Y-%m-%d %H:%M:%S"
    t = datetime.datetime.fromtimestamp(float(epoch) / 1000.)
    return t.strftime(fmt)


def get_epoch_from_datetime(dt):
    """
    Get epoch from datetime.

    :param dt: datetime object
    :return: epoch integer milliseconds
    """
    return int(time.mktime(dt.timetuple()) * 1000)

def get_human_readable_size(nbytes):
    """
    Take bytes and return human readable size format
    :param nbytes: bytes
    :return: human readable size
    """
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 0
    while nbytes >= 1024 and i < len(suffixes) - 1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])