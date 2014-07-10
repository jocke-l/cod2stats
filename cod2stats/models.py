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

    def all(self, table):
        return self.db.select(table)

    def by_id(table¸ id):
        return self.db.where(table, id=id)

    def filter(self, table, **kwargs):
        return self.db.where(table, **kwargs)
