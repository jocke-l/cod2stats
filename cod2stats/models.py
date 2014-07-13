import web

from cod2stats import settings


class Model:
    def __init__(self, db_settings=None):
        if not db_settings:
            db_settings = getattr(settings, 'DATABASE_SETTINGS',
                                  {'db': 'cod2stats',
                                   'user': 'postgres',
                                   'pw': ''})

        self.db = web.database(dbn='postgres', **db_settings)

    def get_players(self, round_id=None):
        if not round_id:
            return self.db.query('SELECT players.id, players.name, \
                                    (SELECT COUNT(*) FROM deaths \
                                     WHERE deaths.killer_id=players.id) \
                                      AS kills, \
                                    (SELECT COUNT(*) FROM deaths \
                                     WHERE deaths.dead_id=players.id) \
                                      AS deaths \
                                  FROM players')

    def get_rounds(self):
        return self.db.query('SELECT rounds.id, rounds.map FROM rounds \
                              ORDER by rounds.id')
