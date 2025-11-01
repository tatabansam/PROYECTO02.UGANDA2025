# PROYECTO02.UGANDA2025
Completed GIS/KML Project: Plotted coordinates in Google Earth, organized into labeled folders. Created 20m-chained routes with elevation profiles, exportable to AutoCAD. Delineated low-terrain polygons, calculating their area in  m 2 . Deliverables: KML/KMZ, AutoCAD files, and Excel/PDF tables.

**Author:** Samantha Sandoval Manrique  
**Year:** 2025  
**Main Tool:** ArcGIS Pro (educational license, Universidad Distrital Francisco José de Caldas)

This project involved a precise terrain slope analysis within a specific area in Uganda. The work was executed based on provided coordinate and visual data, focusing on isolating gentle slopes for specific land-use planning.The initial phase required the manual, point-by-point georeferencing of provided satellite imagery to accurately establish the project boundaries and feature locations.Key Analytical Steps:DEM Generation: Digital Elevation Datasets (DEMs), sourced from USGS satellite imagery, were processed to create a high-resolution slope map of the target area.Slope Classification: The primary goal was the meticulous identification and isolation of low-gradient terrain. Specifically, all areas exhibiting a slope under 3% were classified.Polygon Delineation: These low-slope areas were precisely delineated into distinct, named polygons (e.g., Polygon 1, Polygon 2, etc.) for inventory and planning purposes.Project Deliverables: The final products include the organized polygon mapping, providing an analytical inventory of all terrain below the 3% slope threshold. These deliverables feature accurate area calculations ($\text{m}^2$) for each polygon and are provided in formats compatible with both GIS (KML/KMZ) and CAD overlay.

---

## 📁 Repository structure 
- `/docs`:Full project report.
  
├─ kabwangsi_campus_points (1) - kabwangsi_campus_points.pdf → point-by-point georeferencing

├─ low_pendt_poly_table - low_pend_poly_Table.pdf → Path polygons with areas

└─ elevation_profile_kabwangsi→ Elevation profile 
- `/maps`: Final layout map (PDF).  
- `/data`: Final layers in Shapefile and Autocad format.
- `/scripts`: python code used to generate and calculate lenghts and areas.
- README.md

## 📈 Data sources

- **SU.S. Geological Survey** — .(2025). Digital Elevation Model (DEM) for [Uganda]. [10-31-2025]. Recuperado de https://earthexplorer.usgs.gov/.  
---


## ✅ License and attribution

This repository is released under the **MTI** license.  
All materials are placed in the **public domain**, meaning they may be freely used, modified, and redistributed for any purpose without permission or attribution.

However, proper citation is appreciated when referencing this work:  
> *Samantha Sandoval Manrique — Land Cover Assessment, Boavita (2024)*  
> Data sources: ESA Copernicus.

---

*© Samantha Sandoval Manrique, 2024*

