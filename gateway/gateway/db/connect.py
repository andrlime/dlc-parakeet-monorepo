"""
Connect to a PostgreSQL database using the psycopg2 library and return db object
"""

import psycopg2

from gateway.flask.config import AppConfig


def get_db_connection():
    app_config = AppConfig().config

    return psycopg2.connect(
        database=app_config.get("db_name"),
        host=app_config.get("db_host"),
        user=app_config.get("db_username"),
        password=app_config.get("db_password"),
        port=app_config.get("db_port"),
    )
