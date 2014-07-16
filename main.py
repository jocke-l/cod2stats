#!/usr/bin/env python

import web

from cod2stats.urls import urls
from cod2stats import settings


web.config.debug = getattr(settings, 'DEBUG', True)

app = web.application(urls, globals())
application = app.wsgifunc()

if __name__ == "__main__":
    app.run()
