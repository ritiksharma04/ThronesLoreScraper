import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level= logging.DEBUG,
    filename= "logs/scrape.log",
    encoding="utf-8",
    filemode="a",

    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt= "%Y-%m-%d %H:%M",
)