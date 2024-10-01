import logging
from os import mkdir
from datetime import datetime
from app.settings import settings


class Config:

    token: str = settings.TG_token_bot

    @classmethod
    def start_logger(cls):
        time_format: str = "%d.%m.%Y %H:%M:%S"
        now: str = f"{datetime.now():{time_format}}"
        path_to_filelog: str = f"../logs/{now}.log"
        while 1:
            try:
                logging.FileHandler(path_to_filelog)
                break
            except FileNotFoundError:
                mkdir("../logs")
            except Exception as e:
                exit()
        with open(path_to_filelog, "w") as file:
            file.write(f"{'=' * 55} FILE LOG {'=' * 55}\nTG bot has been started on {now}")
        logging.basicConfig(
            level=logging.INFO,
            filename=path_to_filelog,
            filemode="a",
            format=f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
        )
        attributes = str(Config.__dict__)
        attributes = "\n" + attributes.replace(",", ",\n")
        logging.info(attributes)
