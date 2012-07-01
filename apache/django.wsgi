import os, sys

sys.path.append('/var/www/sitebot.blueearth.net')
sys.path.append('/var/www/sitebot.blueearth.net/sitebot')

os.environ['DJANGO_SETTINGS_MODULE'] = 'sitebot.settings'

import django.core.handlers.wsgi 
application = django.core.handlers.wsgi.WSGIHandler()
