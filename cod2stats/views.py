import web

from cod2stats.models import Model


class View:
   render = web.template.render('cod2stats/templates/', base='base')
   model = Model()


class Index(View):
    def GET(self):
        rounds = self.model.get_rounds()

        return self.render.index(rounds)

class Players(View):
    def GET(self):
        pass
        #players = self.model('players')
        
        #return self.render.players(players)

class Round(View):
    def GET(self, id):
        players = self.model.get_players()

        return self.render.round('Some map', players)

class Player(View):
    def GET(self, id):
        player = Player.filter(id=id)

        return self.render.players(player)
        
