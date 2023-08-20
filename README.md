# FoxAPIWrapper
Foxhole API Wrapper

FoxAPIWrapper is a python wrapper for the offical Foxhole API

https://github.com/clapfoot/warapi

By making a handfull of calls. The wrapper will bring all Foxhole available API data down to a single object:

Function Calls:

  fxWarDataAPI - Pulls down war data.
  
  fxWarMapListDataAPI - Pulls down war map list.
  
  fxWarMapStaticDataAPI - Pulls down static map data.
  
  fxWarReportDataAPI - Pulls down war report data.
  
  fxWarMapRegionDataAPI - Pulls down map region data.

Data Object:

fxWarConquestData - Object that stores all API data

  fxWarData - Overall war data
  
  fxWarMaps - List of maps
  
  fxWarReports - War reports seperated by map name
  
  fxWarMapRegions - Region data seperated by map name
  
  fxWarMapStatics - Region Static data seperated by map name

Refer to fxMain.py for example usage.
