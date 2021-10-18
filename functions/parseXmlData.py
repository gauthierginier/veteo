import xml.etree.ElementTree as ET

def parseXmlData(xmlfile):
    root = ET.parse(xmlfile).getroot()
    res=[]
    for item in root.findall('sl/si'):
        station={}
        station["name"] = item.get('na')[4:]
        station["id"] = item.get('id')
        station["longitude"] = item.get('lg')
        station["latitude"] = item.get('la')
        station["available"] = item.get('av')
        station["from"] = item.get('fr')
        station["to"] = item.get('to')
        res.append(station)
    return res
        
