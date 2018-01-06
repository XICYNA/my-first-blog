import logging

def bar():
        print('I am the bar')

'''def use_logging(func):
        logging.warn('{} is running'.format(func.__name__))
        func()

use_logging(bar)
'''

def use_logging(func):

        def wrapper(*args, **kwargs):
                logging.warn('{} is running'.format(func.__name__))
                return func(*args)
        return wrapper

@use_logging
def foo():
        print('i am foo')

def bar():
        print('i am bar')


