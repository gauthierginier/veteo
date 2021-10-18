from functions.getVelomaggData import getVeloMaggData
from functions.parseXmlData import parseXmlData
import schedule
import time

def getData():
    getVeloMaggData()
    velomaggData = parseXmlData("./velomaggData.xml")
    for i in velomaggData:
        print(i)
schedule.every(1).minutes.do(getData)
while True:
    schedule.run_pending()
    time.sleep(1)