import requests
import logging

def getVeloMaggData():
    velomaggXmlUrl = 'https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_VELOMAG.xml'
    getVelomaggXml = requests.get(velomaggXmlUrl, allow_redirects=True)
    open('velomaggData.xml', 'wb').write(getVelomaggXml.content)
    logging.debug("xml file was downloaded successfuly")
    return True
