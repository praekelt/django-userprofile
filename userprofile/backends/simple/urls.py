from django.conf.urls.defaults import *

from registration.views import activate
from registration.views import register


urlpatterns = patterns('',
    url(r'^register/$',
    register,
    {'backend': 'userprofile.backends.simple.SimpleBackend'},
    name='registration_register'),
)
