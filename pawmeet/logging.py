LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # Important: Don't disable Django's default loggers
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',  # Show DEBUG and above on the console
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'INFO', # Log INFO and above to a file
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'myproject.log'), # Log file location
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': { # Root logger, catches all logs
            'handlers': ['console', 'file'], # Send logs to both console and file
            'level': 'DEBUG', # Log level for the root logger
            'propagate': True, # Important: propagate messages to parent loggers
        },
        'home': { # Logger specific to the 'myapp' app
            'handlers': ['file'], # Only log to file
            'level': 'INFO', # Log level for myapp logger
            'propagate': True, # Important: propagate messages to parent loggers
        },
    },
}