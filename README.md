# FoxAPIWrapper
Foxhole API Wrapper

FoxAPIWrapper is a python wrapper for the official Foxhole API

https://github.com/clapfoot/warapi

By making a handfull of calls. The wrapper will bring all Foxhole available API data down to a single object:

Function Calls:

      fxWarDataAPI - Pulls down war data.
      
      fxWarMapListDataAPI - Pulls down war map list.
      
      fxWarMapStaticDataAPI - Pulls down static map data.
      
      fxWarReportDataAPI - Pulls down war report data.
      
      fxWarMapRegionDataAPI - Pulls down map region data.

Data Object:

fxWarConquestData - Object that stores all API pulled data

      fxWarData - Overall war data
      
      fxWarMaps - List of maps
      
      fxWarReports - War reports separated by map name
      
      fxWarMapRegions - Region data separated by map name
      
      fxWarMapStatics - Region Static data separated by map name

Key Notes:

The following two calls are only required to be ran once as the data is static throughout an entire world conquest war:

      fxWarMapListDataAPI
      
      fxWarMapStaticDataAPI

The following four calls can be ran multiple times as the data can go stale:

      fxWarDataAPI
      
      fxWarMapStaticDataAPI

      fxWarReportDataAPI

      fxWarMapRegionDataAPI


eTag:

The following two calls are built to respect eTag headers as requested by the developers in their official API documentation. The calls will check eTags before doing a new request for data. In some scenarios data pulled hours earlier might still be up to date. This prevents unnecessary data requests:

      fxWarReportDataAPI
      
      fxWarMapRegionDataAPI
