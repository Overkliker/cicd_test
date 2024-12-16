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

TOKEN = config["bot"]["TOKEN"].replace("'", "")
