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
        return self.db.query('SELECT rounds.id, rounds.map \
                              FROM rounds                  \
                              WHERE rounds.id = $round_id  \
                              ORDER BY rounds.id DESC',
                             {'round_id': round_id})

    def get_players(self, round_id=None, player_id=None, limit=None):
        if round_id:
            return self.db.query('SELECT                                  \
                                    players.id, players.name,             \
                                    roundplayers.playtime,                \
                                    roundplayers.kills,                   \
                                    roundplayers.deaths,                  \
                                    POWER(roundplayers.kills, 2) * 60 /   \
                                        EXTRACT(epoch FROM                \
                                                roundplayers.playtime)    \
                                      AS efficancy                        \
                                  FROM rounds, roundplayers, players      \
                                  WHERE                                   \
                                    rounds.id = $round_id AND             \
                                    roundplayers.round_id = rounds.id AND \
                                    roundplayers.player_id = players.id   \
                                    {0}                                   \
                                  ORDER BY efficancy DESC                 \
                                  {1}'                                    \
                                    .format('AND players.id = $player_id' \
                                              if player_id else '',
                                            'LIMIT $limit'                \
                                              if limit else ''),
                                 {'round_id': round_id,
                                  'player_id': player_id,
                                  'limit': limit})
        else:
            return self.db.query('SELECT                                \
                                    players.id, players.name,           \
                                    players.kills, players.deaths,      \
                                    players.playtime,                   \
                                    POWER(players.kills, 2) * 60 /      \
                                        EXTRACT(epoch FROM              \
                                                players.playtime)       \
                                      AS efficancy                      \
                                  FROM players                          \
                                  {0}                                   \
                                  ORDER BY efficancy DESC               \
                                  {1}'                                  \
                                    .format('WHERE                      \
                                               players.id = $player_id' \
                                              if player_id else '',
                                            'LIMIT $limit'              \
                                              if limit else ''),
                                  {'player_id': player_id,
                                   'limit': limit})

    def get_rounds(self):
        return self.db.query('SELECT rounds.id, rounds.map,               \
                                (SELECT roundplayers.playtime             \
                                 FROM roundplayers                        \
                                 WHERE roundplayers.round_id = rounds.id  \
                                 LIMIT 1) AS playtime                     \
                              FROM rounds                                 \
                              ORDER by rounds.id ASC')
