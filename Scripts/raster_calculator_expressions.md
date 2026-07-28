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
