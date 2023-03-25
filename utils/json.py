import json
import logging

def create_config() -> None:
    default_config = {
        "gebruikersnaam":"",
        "wachtwoord":"",
    }
    with open("config.json", "w") as file:
        try:
            json.dump(default_config, file, indent=4)
            logging.info("Created blank config file.")
        except IOError:
            logging.error("Error creating config file.")

def read_config() -> dict:
    with open("config.json", "r") as file:
        return json.load(file)
