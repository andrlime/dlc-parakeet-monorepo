"""
Helper functions to configure Flask app settings
"""

import os

from dotenv import load_dotenv
from yaml import load, Loader

from gateway.exceptions import ConfigValueError


class AppConfig(object):
    """
    Singleton AppConfig class to read config from .env and config.yml and
    return a single dictionary with those values
    """

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(AppConfig, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        if not hasattr(self, "config"):
            load_dotenv()

            yml_config = self.read_yaml_config_file("config.yaml")
            db_config = yml_config.get("db")
            app_config = yml_config.get("app")

            self.config = {
                "app_port": self.get_key(app_config, "app_port", "config.yml"),
                "db_name": self.get_key(db_config, "db_name", "config.yml"),
                "db_host": self.get_key(db_config, "db_host", "config.yml"),
                "db_port": self.get_key(db_config, "db_port", "config.yml"),
                "db_username": self.get_key(os.environ, "PARAKEET__DB_USERNAME", ".env"),
                "db_password": self.get_key(os.environ, "PARAKEET__DB_PASSWORD", ".env"),
            }

    def get_key(self, obj: dict, key: str, place: str):
        try:
            return obj.get(key)
        except ValueError as e:
            raise ConfigValueError(f"{key} not set in {place}") from e

    def read_yaml_config_file(self, path: str):
        """
        Read DB config from the config.yml file
        """

        stream = open(path, "r", encoding="utf-8")
        content = load(stream, Loader)
        stream.close()

        return content
