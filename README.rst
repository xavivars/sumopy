sumopy: Python Sumologic Logging HTTP Handler
=============================================

**sumopy** is a Python library that provides a logging handler that eases pushing logs to Sumologic.

It can be used as any other Python handler, by defining its configuration
(in code, in a dictionary or in a configuration file).

As part of the configuration, source_name can be overwritten, and URL path has to be injected
(host is not needed). URL will look like ``/receiver/v1/http/LONG_HASH``

Here you have how to push standard raw text messages to Sumologic
Logging as txt::

    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)-8s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        }
    },
    'handlers': {
        'sumologger': {
            'source_name': 'sumopy_test',
            'level': 'INFO',
            'class': 'sumopy.Handler',
            'url': 'YOUR_ENDPOINT_PATH_HERE,
            'formatter': 'default'
        }
    },
    'loggers': {
        '': {
            'handlers': ['sumologger'],
        }
    }

**sumopy** also allows you to use JSON formatters, transparently sending them as JSON to sumologic

Here you have an example, using the *pythonjsonlogger* library to define the formatter, and then using it 
to push logs using the *sumopy.Handler*::

    'formatters': {
        'json': {
            'format': '%(message)s %(levelname)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'class': 'pythonjsonlogger.jsonlogger.JsonFormatter'
        }
    },
    'handlers': {
        'sumologger': {
            'source_name': 'sumopy_test',
            'level': 'INFO',
            'class': 'sumopy.Handler',
            'url': 'YOUR_ENDPOINT_PATH_HERE',
            'formatter': 'json'
        }
    },
    'loggers': {
        '': {
            'handlers': ['sumologger'],
        }
    }

