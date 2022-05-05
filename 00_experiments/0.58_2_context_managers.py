"""
NOTE!!! This is just PROTOTYPE, not real code to work
url to work with: https://www.postgresqltutorial.com/postgresql-python/connect/
"""

import contextlib
import psycopg2


@contextlib.contextmanager
def database_context(**kwargs):
    """
    Creates connection to PostgreSQL server,
    allow the user to run some code, and closes db connection.

    kwargs:
      dbname
      user
      password
      host
    """
    # set up database connection
    conn = psycopg2.connect(dbname='database', user='db_user',
                            password='mypassword', host='localhost')
    yield conn

    # tear down database connection


if __name__ == '__main__':
    print(f'current directory: {os.getcwd()}')
    # say, file we need is located at: '/home/kav/kinozal.tv'

    with in_dir('/home/kav'):
        with open('kinozal.tv', 'r') as f:
            data = f.read().strip()
    print(f'data: {data.split()}')
    print(f'current directory: {os.getcwd()}')

