import json
import time


def print_test_time_elapsed(method):
    def run(*args, **kw):
        ts = time.time()
        print('\n\ttesting function %r' % method.__name__)
        method(*args, **kw)
        te = time.time()
        print('\t[OK] in %r %2.10f sec' % (method.__name__, te - ts))

    return run
