import configparser
import os

config = configparser.ConfigParser()

path = os.getcwd()
split_path = os.getcwd().split("\\")
count_of_slashes = 0

for i in range(len(split_path)):
    if split_path[i] == "AI-assistant":
        count_of_slashes = len(split_path[i:-1])
        break

config.read(os.getcwd() + "\\.." * count_of_slashes + "\\config.ini")

DB_HOST = str(config["api"]["DB_HOST"].replace("'", "").replace('"', ""))
DB_PORT = config["api"]["DB_PORT"].replace("'", "").replace('"', "")
DB_NAME = str(config["api"]["DB_NAME"].replace("'", "").replace('"', ""))
DB_USER = str(config["api"]["DB_USER"].replace("'", "").replace('"', ""))
DB_PASS = str(config["api"]["DB_PASS"].replace("'", "").replace('"', ""))


# DB_HOST="localhost"
# DB_PORT="5432"
# DB_NAME="assist_api_db"
# DB_USER="postgres"
# DB_PASS="1234"