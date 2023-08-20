import requests
from requests.adapters import HTTPAdapter, Retry
from fxAPIData import *
from fxAPI import *


 #API URLS
fxApiWarUrl = "https://war-service-live.foxholeservices.com/api/worldconquest/war"
fxApiWarMapsUrl = "https://war-service-live.foxholeservices.com/api/worldconquest/maps/"
fxApiWarReportURL = "https://war-service-live.foxholeservices.com/api/worldconquest/warReport/"

#Create War Data Object
fxWarConquest = fxWarConquestData()

#Create session object
fxSession = requests.Session()
fxRetries = Retry(total=5, backoff_factor=1, status_forcelist=[ 502, 503, 504 ])
fxSession.mount('http://', HTTPAdapter(max_retries=fxRetries))

#Pull War List
fxWarDataAPI(fxSession, fxApiWarUrl, fxWarConquest)

#Pull Map List (this only needs to be ran once per war or if data is not being cached for future use)
fxWarMapListDataAPI(fxSession, fxApiWarMapsUrl, fxWarConquest)

#Pull Static Data (this only needs to be ran onc eper war or if the data is not being cached for future use)
for mapName in fxWarConquest.fxWarMaps.maps:
    fxWarMapStaticDataAPI(fxSession, (fxApiWarMapsUrl + mapName + "/static"), mapName, fxWarConquest)

#Pull Casualty and Region Data
for mapName in fxWarConquest.fxWarMaps.maps:
    fxWarReportDataAPI(fxSession, (fxApiWarReportURL + mapName), mapName, fxWarConquest)
    fxWarMapRegionDataAPI(fxSession, (fxApiWarMapsUrl + mapName + "/dynamic/public"), mapName, fxWarConquest)
    
#Close Session
fxSession.close()


