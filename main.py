from functions.getVelomaggData import getVeloMaggData
from functions.parseXmlData import parseXmlData
import schedule
import time
import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
        handlers=[RotatingFileHandler('./logs/logs.log', maxBytes=100000, backupCount=10)],
        level=logging.DEBUG,
        format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
        datefmt='%Y-%m-%dT%H:%M:%S')


def getData():
    getVeloMaggData()
    velomaggData = parseXmlData("./velomaggData.xml")
    for i in velomaggData:
        print(i)


getData()
schedule.every(1).minutes.do(getData)

while True:
    schedule.run_pending()
    time.sleep(1)