from sqlalchemy import inspect, create_engine
from sqlalchemy.engine.reflection import Inspector

engine = create_engine('sqlite:////media/chris/Data/dev/sqlalchemy_dynamic_models/db/data.db')


def inspect_db():
    insp = inspect(engine)
    return insp


def refresh_model(table_name: str):
    # Get schema and extract the required column names
    inspector = Inspector.from_engine(engine)
    db_columns = inspector.get_columns(table_name, schema='main')
    new_model_columns = []
    for column in db_columns:
        new_model_columns.append(tuple([str(column['name']),
                                        str(column['type']),
                                        column['nullable'],
                                        column['default'],
                                        column['autoincrement'],
                                        column['primary_key']]))
    new_model_columns_dict = {}
    for column in db_columns:
        new_model_columns_dict.setdefault(column['name'], []).append(str(column['type']))
    # new_model_columns_list = []
    # for column in db_columns:
    #     new_model_columns_list.append([
    #         ['name', column['name']],
    #         ['type', str(column['type'])],
    #         ['nullable', column['nullable']],
    #         ['default', column['default']],
    #         ['autoincrement', column['autoincrement']],
    #         ['primary_key', column['primary_key']]])

    return new_model_columns_dict
