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

    def get_map(self, round_id):
        return self.db.query('SELECT map FROM rounds     \
                              WHERE round_id = $round_id',
                             {'round_id': round_id})

    def get_players(self, round_id=None, limit=None):
        if round_id:
            return self.db.query('SELECT                                  \
                                    players.id, players.name,             \
                                    roundplayers.playtime,                \
                                    roundplayers.kills,                   \
                                    roundplayers.deaths,                  \
                                    POWER(roundplayers.kills, 2)*60 /     \
                                        EXTRACT(\'epoch\' FROM            \
                                                roundplayers.playtime)    \
                                      AS efficancy                        \
                                  FROM rounds, roundplayers, players      \
                                  WHERE                                   \
                                    rounds.id = $round_id AND             \
                                    roundplayers.round_id = rounds.id AND \
                                    roundplayers.player_id = players.id   \
                                  ORDER BY efficancy DESC'                \
                              + ('LIMIT $limit' if limit else ''),
                                 {'round_id': round_id,
                                  'limit': limit})
        else:
            return self.db.query('SELECT                           \
                                    players.id,                    \
                                    players.kills, players.deaths, \
                                    POWER(players.kills,2 )*60 /   \
                                        EXTRACT(\'epoch\' FROM     \
                                                players.playtime)  \
                                      AS efficancy                 \
                                  FROM players'                    \
                              + ('LIMIT $limit' if limit else ''),
                                 {'limit': limit})

    def get_rounds(self):
        return self.db.query('SELECT rounds.id, rounds.map FROM rounds \
                              ORDER by rounds.id')
