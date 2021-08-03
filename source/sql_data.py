from sqlalchemy import create_engine
import pandas as pd


def get_sql_df(table_name, connection_string):
    """

    :param table_name: Provide a valid table name.
    :param connection_string: Provide valid sqlalchemy connection string. For e.g. 'postgres:///db_name'
    :return:
    """
    # cnx = sqlite3.connect('foo')
    cnx = create_engine(connection_string)
    return pd.read_sql_table(table_name, cnx)
