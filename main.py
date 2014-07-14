#!/usr/bin/env python

import web

from cod2stats.urls import urls

app = web.application(urls, globals())
application = app.wsgifunc()

if __name__ == "__main__":
    app.run()
