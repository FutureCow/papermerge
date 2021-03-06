from .base import *  # noqa

DEBUG = True


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'ocr.log',
            'level': 'DEBUG'
        },
        'file_core': {
            'class': 'logging.FileHandler',
            'filename': 'core.log',
            'level': 'DEBUG'
        }
    },
    'loggers': {
        'papermerge': {
            'handlers': ['console'],
            'level': 'DEBUG'
        },
        'celery': {
            'handlers': ['console'],
            'level': 'INFO'
        },
        'papermerge.core.ocr': {
            'handlers': ['file'],
            'level': 'DEBUG'
        },
        'mglib': {
            'handlers': ['file'],
            'level': 'DEBUG'
        },
        'papermerge.core': {
            'handlers': ['file_core'],
            'level': 'DEBUG'
        }
    },
}
