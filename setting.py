"""
giving parser and all information for setting database
"""
import argparse
import os
from urllib.parse import urlparse

parser = argparse.ArgumentParser()

DBHOST = os.getenv('DBHOST', 'localhost')

parser.add_argument("--dbtype",
                    help="Database drivername",
                    default='postgres')

parser.add_argument("-p","--password",
                    help="Database password",
                    default='pass')

parser.add_argument("-dbport","--port",
                    help="Database port",
                    default=5432)

parser.add_argument("-dbhost","--host",
                    help="Database hort",
                    default=DBHOST)

parser.add_argument("--username", default="postgres")
parser.add_argument("--dbname", default="postgres")

args = parser.parse_args()