class ProductionConfig(object):
    """A basic production config
    """
    TRYTON_DATABASE = 'health30' #Change
    SECRET_KEY = 'gnuhealth'    #Change
    SERVER_NAME = "localhost.localdomain:5000"     #Set this
    TRYTON_CONFIG = '/etc/tryton/trytond.conf'

    PREFERRED_URL_SCHEME='https'
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_NAME = 'fhir'
    PERMANENT_SESSION_LIFETIME = 24*60*60 #seconds

    #Remember Me setup
    REMEMBER_COOKIE_NAME='fhir_remember_token'
    #REMEMBER_COOKIE_DURATION #default 1 year

class DebugConfig(object):
    """Testing settings"""
    TRYTON_DATABASE='gnuhealth_demo_test'
    DEBUG = True
    SECRET_KEY = 'test'
    WTF_CSRF_ENABLED=False
    SESSION_COOKIE_NAME = 'fhir'
    REMEMBER_COOKIE_NAME='fhir_remember_token'
