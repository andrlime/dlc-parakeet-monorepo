"""
All blueprints imported in one module
"""

from gateway.db.api import bp as db
from gateway.pair.api import bp as pair
from gateway.parser.api import bp as parser


def all_blueprints():
    return [("db", db), ("pair", pair), ("parser", parser)]
