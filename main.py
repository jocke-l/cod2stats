#!/usr/bin/env python

import web

from cod2stats.urls import urls

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
