import timeit

import pandas as pd
from sql_data import get_sql_df
import os
from dotenv import load_dotenv

load_dotenv()

db_search = os.getenv('DB_SEARCH')
table_name = os.getenv('TABLE_NAME')
connection_string = os.getenv('CONNECTION_STRING')
flat_file = os.getenv('FLAT_FILE_DATA')


def search_address():
    search = input('Enter the name you want to search : ')
    flat_df = pd.read_csv(flat_file, header=None, names=["First Name", "Last Name", "Address", "City", "State", "Age"])
    flat_df = pd.concat(ignore_index=True, objs=[get_sql_df(table_name, connection_string), flat_df]) \
        if db_search == 'on' else flat_df
    result_df = flat_df[(flat_df['First Name'].str.contains(search, case=False))
                        | (flat_df['Last Name'].str.contains(search, case=False))]
    print(result_df.to_dict(orient='index'))
    return result_df.to_dict(orient='index')


print(f"Time taken={timeit.timeit('search_address()', setup='from __main__ import search_address', number=1)}")
