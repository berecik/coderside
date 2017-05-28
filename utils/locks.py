# -*- coding: utf-8 -*-
__author__ = 'beret'

import os
import fcntl
import threading


class SharedCounter:
    '''
    A counter object that can be shared by multiple threads.
    '''
    def __init__(self, initial_value=0):
        self._value = initial_value
        self._value_lock = threading.Lock()

    def incr(self, delta=1):
        '''
        Increment the counter with locking
        '''
        with self._value_lock:
             self._value += delta

    def decr(self, delta=1):
        '''
        Decrement the counter with locking
        '''
        with self._value_lock:
             self._value -= delta


class DjangoLock:
    """
    Usage:

        lock = DJangoLock('/tmp/djangolock.tmp')
        lock.acquire()
        try:
            pass
        finally:
            lock.release()
    """
    def __init__(self, filename):
        self.filename = filename
        # This will create it if it does not exist already
        self.handle = open(filename, 'w')

    # flock() is a blocking call unless it is bitwise ORed with LOCK_NB to avoid blocking
    # on lock acquisition.  This blocking is what I use to provide atomicity across forked
    # Django processes since native python locks and semaphores only work at the thread level
    def acquire(self):
        fcntl.flock(self.handle, fcntl.LOCK_EX)

    def release(self):
        fcntl.flock(self.handle, fcntl.LOCK_UN)

    def __del__(self):
        self.handle.close()

