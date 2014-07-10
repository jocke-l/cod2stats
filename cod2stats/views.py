import web

class index:
    def GET(self):
        render = web.template.render('cod2stats/templates')

        return render.index()
