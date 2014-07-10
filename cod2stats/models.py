import web

from cod2stats import settings


class Model:
    def __init__(self, db_settings=None):
        if not db_settings:
            db_settings = getattr(settings, 'DATABASE_SETTINGS',
                                  {'db': 'default',
                                   'user': 'postgres',
                                   'pw': ''})

        self.db = web.database(dbn='postgres', **db_settings)


    # Future stuff
