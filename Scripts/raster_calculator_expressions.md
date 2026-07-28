# 🧮 QGIS Raster Calculator Expressions & Spectral Algorithms
**Project:** Post-Monsoon Inundation and Waterlogging Analysis of Barpeta District, Assam (2024 vs 2025)  
**Author / GIS Analysis:** Shivam Shukla  
**Software Compatibility:** QGIS 3.x (GDAL / QgsRasterCalculator)

---

## 1. Normalized Difference Water Index (NDWI) Computation
The NDWI is derived from Sentinel-2 Level-2A multispectral imagery using Band 3 (Green - 560 nm) and Band 8 (Near-Infrared / NIR - 842 nm) at a 10m spatial resolution.

### Mathematical Formula:
$$NDWI = \frac{\text{Green} - \text{NIR}}{\text{Green} + \text{NIR}}$$

### QGIS Raster Calculator Expression:
```ini
("Sentinel2_2024_B03@1" - "Sentinel2_2024_B08@1") / ("Sentinel2_2024_B03@1" + "Sentinel2_2024_B08@1")
```
*(Note: Replace `2024` with `2025` for the comparative assessment year).*

---

## 2. Atmospheric Filtering via Scene Classification Layer (SCL)
To prevent false water positives from cloud shadows and atmospheric interference, Sentinel-2 SCL masking was applied. Pixel values **3 (Cloud shadow)**, **8 (Cloud medium probability)**, and **9 (Cloud high probability)** were assigned as `NoData` (-9999).

### QGIS Raster Calculator Expression (Conditional Masking):
```ini
if("Sentinel2_2024_SCL@1" = 3 or "Sentinel2_2024_SCL@1" = 8 or "Sentinel2_2024_SCL@1" = 9, -9999, "NDWI_2024@1")
```
*(Note: Any pixel evaluating to -9999 is subsequently rendered transparent by setting the NoData value in QGIS raster properties).*

---

## 3. Binary Water Masking (Thresholding)
A binary threshold of $NDWI > 0$ was applied to the cloud-free NDWI raster to segregate positive surface inundation from dry land and dense vegetation.

### QGIS Raster Calculator Expression:
```ini
if("Cloud_Free_NDWI_2024@1" > 0, 1, 0)
```
* **Output Value `1`:** Positive surface inundation / permanent water body.
* **Output Value `0`:** Non-water land / dry vegetation.

---

## 4. Multi-Temporal Change Detection & Drainage Recovery (2024 vs 2025)
To quantify the net recession of waterlogged areas over the 1-year observation period, a raster subtraction model was executed between the two binary masks.

### Mathematical Formula:
$$\Delta \text{Water} = \text{Flood\_Mask\_2025} - \text{Flood\_Mask\_2024}$$

### QGIS Raster Calculator Expression:
```ini
"Flood_Mask_2025@1" - "Flood_Mask_2024@1"
```

### Interpretation of Output Raster Values:
| Pixel Value | Hydrological Meaning | Cartographic Symbology |
| :---: | :--- | :--- |
| **`-1`** | **Recovered / Drained Land** (Water in 2024, Dry in 2025) | High-Contrast Magenta (`#E600E6`) to Dry Transition |
| **`0`** | **Stable State** (Permanent Beels/Wetlands or Dry Land) | Transparent / No Change |
| **`+1`** | **New Inundation** (Dry in 2024, Flooded in 2025) | Vivid Cyan (`#00E6E6`) |

---

## 5. Post-Processing: Spatial Clipping & NoData Handling
To ensure exact pixel counts matching the administrative boundary of Barpeta District (excluding external buffer zones and atmospheric borders), rasters were clipped using the vectorized district boundary (`Barpeta_Boundary.geopkg`).

### GDAL / QGIS Processing Syntax (Clip Raster by Mask Layer):
```text
Algorithm: gdal:cliprasterbymasklayer
Input Layer: Binary_Water_Mask@1
Mask Layer: Barpeta_District_AOI (.geopkg)
Assign specified NoData value to output bands: -9999
Match the extent of the clipped raster to the mask layer: Yes (True)
```
