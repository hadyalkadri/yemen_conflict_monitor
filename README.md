# Yemen Conflict & Humanitarian Access Monitor 🇾🇪

An end-to-end data engineering and spatial analysis project that transforms raw conflict data into executive-level humanitarian intelligence.

## 🔗 Live Interactive Dashboard
[**Click here to view the Interactive Tableau Dashboard**](https://public.tableau.com/views/YemenConflictMonitorProject-Dashboard/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

---

## 📌 Executive Summary
This project provides a standardized framework for monitoring conflict intensity in Yemen. By aggregating point-based incident data into 11km hexagonal bins, the monitor identifies high-risk zones while adhering to humanitarian protection standards (anonymizing specific GPS locations).

## 🛠️ Technical Stack
* **Data Processing:** Python (Pandas, Geopandas, Pathlib)
* **GIS & Spatial Analysis:** QGIS (Geometry cleaning, Hex-gridding, Spatial Joins)
* **Business Intelligence:** Tableau Public
* **Data Source:** ACLED (Armed Conflict Location & Event Data Project) and  Humanitarian Data Exchange (Spatial Boundaries)

## 📂 Project Structure
```text
Parent Dir/
|   
+---data
|   +---processed
|   |   |   processed_incidents.json
|   |   |   
|   |   \---spatial
|   |           Yemen_Conflict_Data_QGIS.geojson
|   |           
|   \---raw
|       |   data.csv
|       |   
|       \---spatial
|               yem_admin0.prj
|               yem_admin0.shp
|               yem_admin1.prj
|               yem_admin1.shp
|               yem_adminlines.prj
|               yem_adminlines.shp
|               yem_adminpoints.prj
|               yem_adminpoints.shp
|               
+---docs
|   \---visuals
|           dashboard.png
|           dashboard_hover.png
|           qgis_layers.png
|           
\---scripts
        index.py
└── README.md
