"""
giving parser and all information for setting database
"""
import argparse
import os

parser = argparse.ArgumentParser()

DB_HOST = os.getenv('DB_HOST', 'localhost')

parser.add_argument("-db_type", "--dbtype", help="Database drivername", default='postgres')

parser.add_argument("-p", "--password", help="Database password", default='pass')

parser.add_argument("-db_port", "--port", help="Database port", default=5432)

parser.add_argument("-db_host", "--host", help="Database hort", default=DB_HOST)

parser.add_argument("-u", "--username", help="Database username", default="postgres")

parser.add_argument("-db_name", "--dbname", help="Name of database", default="postgres")

args = parser.parse_args()
