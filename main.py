from functions.getVelomaggData import getVeloMaggData
from functions.parseXmlData import parseXmlData

getVeloMaggData()
velomaggData = parseXmlData("./velomaggData.xml")
for i in velomaggData:
    print(i)