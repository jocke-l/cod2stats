import web

from cod2stats.models import Model

class View:
    globals = {}
    render = web.template.render('cod2stats/templates/',
                                 globals=globals,
                                 base='base')
    model = Model()

    # Little trick to include other templates from within templates
    # Usage: $:include.template(args, ...)
    globals['include'] = web.template.render('cod2stats/templates/',
                                             globals=globals)


class Index(View):
    def GET(self):
        players = self.model.get_players(limit=10)

        return self.render.players('Top 10 players', players)

class Rounds(View):
    def GET(self):
        rounds = self.model.get_rounds()

        return self.render.rounds(rounds)

class Round(View):
    def GET(self, id):
        players = self.model.get_players(round_id=id)
        map_name = self.model.get_map(id)[0]['map']

        return self.render.players(map_name, players)

class Players(View):
    def GET(self):
        players = self.model.get_players()
        
        return self.render.players('Players', players)

class Player(View):
    def GET(self, id):
        player = self.model.get_players(player_id=id)

        return self.render.players('Player', player)
