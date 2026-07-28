## 📊 Quantitative Methodology & Geospatial Computation

This section details the pixel-level computational rigor applied during the remote sensing analysis of Barpeta District using QGIS Raster Statistics and Sentinel-2 Level-2A imagery.

### 1. Geospatial Layer Metadata & Projection Standards
All raster processing and statistical extractions were performed under unified cartographic parameters to ensure strict spatial alignment across multi-temporal datasets:

* **Coordinate Reference System (CRS):** EPSG:32646 - WGS 84 / UTM Zone 46N
* **Spatial Resolution:** 10 meters per pixel (1 Pixel = 10m x 10m = 100 sq. meters)
* **Raster Dimensions:** 6,311 x 5,955 pixels (Total grid capacity: 37,582,005 pixels per raster scene)

---

### 2. Comparative Raster Layer Statistics (QGIS Report Summary)

The thematic water masks (`Flood_Mask_2024.tif` and `Flood_Mask_2025.tif`) were analyzed using automated raster layer computation. The pixel distributions represent:
* **Value 1 (Water Mask):** Positively identified surface inundation and permanent water bodies via NDWI thresholding.
* **Value 0 (Non-Water):** Dry land, vegetation, and built-up areas.
* **NoData Pixels:** Filtered cloud cover, atmospheric interference (via SCL masking), and areas outside the administrative boundary of Barpeta district.

| Raster Layer / Year | Pixel Classification | Pixel Count | Surface Area (m²) | Area (Sq. Km.) |
| :--- | :--- | :---: | :---: | :---: |
| **2024 Baseline** (`Flood_Mask_2024.tif`) | **Value 1 (Inundated Water)** | **3,531,094** | **353,109,400 m²** | **353.11 Sq. Km.** |
| | Value 0 (Non-Water Land) | 13,946,032 | 1,394,603,200 m² | 1,394.60 Sq. Km. |
| | *NoData (Masked / Outside)* | *20,104,879* | *—* | *—* |
| **2025 Assessment** (`Flood_Mask_2025.tif`) | **Value 1 (Inundated Water)** | **2,819,778** | **281,977,800 m²** | **281.98 Sq. Km.** |
| | Value 0 (Non-Water Land) | 12,341,923 | 1,234,192,300 m² | 1,234.19 Sq. Km. |
| | *NoData (Masked / Outside)* | *22,420,304* | *—* | *—* |

---

### 3. Step-by-Step Mathematical Derivation

#### Step 1: Pixel-to-Area Conversion Formula
Since Sentinel-2 imagery provides a 10m ground sampling distance, each pixel represents an area of 100 square meters. To convert the raw pixel counts into standardized square kilometers:

`Area (Sq. Km.) = (Total Pixels * 100) / 1,000,000`

#### Step 2: Post-Monsoon Surface Water Extent Calculation
* **2024 Peak Extent:** `(3,531,094 pixels * 100) / 1,000,000` = **353.11 Sq. Km.**
* **2025 Comparative Extent:** `(2,819,778 pixels * 100) / 1,000,000` = **281.98 Sq. Km.**

#### Step 3: Hydrological Recovery and Drainage Quantification
To evaluate the natural drainage recovery and recession of waterlogged floodplains over the 1-year observation period:

* **Net Inundation Reduction:** `281.98 Sq. Km. - 353.11 Sq. Km.` = **-71.13 Sq. Km.**
* **Percentage Recovery Rate:** `(|-71.13| / 353.11) * 100` = **20.14% Overall Drainage Recovery**

> **Conclusion:** The automated QGIS raster computation validates a substantial **20.14% reduction** in surface waterlogged extent across Barpeta district between October 2024 and October 2025, demonstrating significant hydrological recovery along the Brahmaputra floodplain network.
