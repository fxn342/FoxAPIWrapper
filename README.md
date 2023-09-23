# FoxAPIWrapper
**Foxhole API Wrapper**

FoxAPIWrapper is a python wrapper for the official Foxhole API

https://github.com/clapfoot/warapi

**Discord for FoxAPIWrapper**

https://discord.gg/NpEE3hwz

**To Do**

Add logging library.

**Details**

The wrapper was built around the idea that a single object would store all Foxhole API data which can then be linked together using either the map name or region ID as a key.

**Function Calls:**

      fxWarDataAPI - Pulls down war data.
      
      fxWarMapListDataAPI - Pulls down war map list.
      
      fxWarMapStaticDataAPI - Pulls down static map data.
      
      fxWarReportDataAPI - Pulls down war report data.
      
      fxWarMapRegionDataAPI - Pulls down map region data.

**Data Object:**

fxWarConquestData - Object that stores all API pulled data

      fxWarData - Overall war data
      
      fxWarMaps - List of maps
      
      fxWarReports - War reports separated by map name
      
      fxWarMapRegions - Region data separated by map name
      
      fxWarMapStatics - Region Static data separated by map name

**Key Notes:**

The following two calls are only required to be ran once as the data is static throughout an entire world conquest war:

      fxWarMapListDataAPI
      
      fxWarMapStaticDataAPI

The following four calls can be ran multiple times as the data can go stale:

      fxWarDataAPI
      
      fxWarMapStaticDataAPI

      fxWarReportDataAPI

      fxWarMapRegionDataAPI


**eTag:**

The following two calls are built to respect eTag headers as requested by the developers in their official API documentation. The calls will check eTags before doing a new request for data. In some scenarios data pulled hours earlier might still be up to date. This prevents unnecessary data requests:

      fxWarReportDataAPI
      
      fxWarMapRegionDataAPI

**Sample Code**

Refer to fxMain.py for sample usage. The code demos how to create fields for API URLS, creating a request session and how to loop through the different API calls to pull down all API data.
