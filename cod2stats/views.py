import web

from cod2stats.models import Model

class index:
    def GET(self):
        model = Model()
        render = web.template.render('cod2stats/templates')

        return render.index(model.db.query('select * from rounds'))
