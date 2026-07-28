# 🌊 Post-Monsoon Inundation and Waterlogging Analysis of Barpeta District, Assam (2024 vs 2025)

![GIS](https://img.shields.io/badge/GIS-QGIS%203.x-2980b9?style=for-the-badge&logo=qgis&logoColor=white)
![Remote Sensing](https://img.shields.io/badge/Remote%20Sensing-Sentinel--2-27ae60?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![Region](https://img.shields.io/badge/Region-Assam%2C%20India-e67e22?style=for-the-badge)

## 📌 Project Overview
This geospatial research project provides a comprehensive comparative analysis of post-monsoon surface inundation and persistent waterlogging in **Barpeta district, Assam** between **October 22, 2024**, and **October 22, 2025**. 

Using high-resolution **Sentinel-2 Level-2A** multispectral satellite imagery, surface water was delineated using the **Normalized Difference Water Index (NDWI)** combined with advanced **Scene Classification Layer (SCL)** cloud-masking techniques. The study quantifies natural drainage recovery, monitors low-lying floodplain retention along the Brahmaputra basin, and maps perennial wetland networks (*Beels*).

---

## 📊 Key Findings & Quantitative Analysis

| Metric / Parameter | 2024 (Baseline Peak) | 2025 (Comparative Assessment) | Net Change / Recovery |
| :--- | :---: | :---: | :---: |
| **Observation Date** | October 22, 2024 | October 22, 2025 | — |
| **Total Inundated Area** | **353.11 Sq. Km.** | **281.98 Sq. Km.** | **-71.13 Sq. Km.** |
| **Drainage / Recovery Rate** | — | — | **~20.1% Reduction ↓** |
| **Cloud/Shadow Masked** | Minimal Atmospheric Noise | 22,420,304 Pixels (SCL Masked) | Transparent Exclusion |

> **Highlight:** The district experienced a significant drainage recovery of **20.1%** in surface waterlogged area in 2025 compared to the 2024 post-monsoon baseline.

---

## 🛠️ Data Sources & Technical Stack

* **Satellite Imagery:** ESA Copernicus Sentinel-2 (Level-2A Bottom of Atmosphere Reflectance)
* **Spatial Resolution:** 10 meters (Band 3 - Green, Band 8 - Near Infrared)
* **Coordinate Reference System (CRS):** `EPSG:32646` (WGS 84 / UTM Zone 46N)
* **GIS Software Used:** QGIS (Desktop & Print Layout Engine)
* **Cartographic Accent:** HTML/CSS-styled layout widgets & False-Color / Thematic Binary Masking

---

## ⚙️ Step-by-Step Methodology

### Step 1: Data Acquisition & Preprocessing
1. Downloaded Sentinel-2 L2A tiles covering Barpeta district for **October 22, 2024**, and **October 22, 2025** from the Copernicus Open Access Hub / Browser.
2. Mosaicked and clipped the raster bands (`B03`, `B08`, and `SCL`) using the official administrative vector boundary of Barpeta district.

### Step 2: Atmospheric Correction & Cloud Masking (SCL)
To prevent cloud shadow false-positives in water detection, advanced masking was executed using the **Scene Classification Layer (SCL)** in QGIS Raster Calculator:
* **Excluded Classes:** Value `3` (Cloud Shadows), Value `8` (Cloud Medium Probability), and Value `9` (Cloud High Probability).
* Successfully removed over **2.24 crore interfering pixels** from the 2025 dataset to ensure 100% cloud-free surface reflectance.

### Step 3: NDWI Computation & Binary Thresholding
Calculated the **Normalized Difference Water Index (NDWI)** to isolate open surface water and waterlogged agricultural soil:
$$\text{NDWI} = \frac{\text{Green (B03)} - \text{NIR (B08)}}{\text{Green (B03)} + \text{NIR (B08)}}$$

* Applied binary classification where **$\text{NDWI} > 0$** was classified as `1` (Water / Inundated) and **$\text{NDWI} \le 0$** as `0` (Non-Water / Dry Land).

### Step 4: Area Calculation & Zonal Statistics
* Utilized QGIS **Unique Values Report** and Raster Layer Statistics to calculate pixel counts for Value `1`.
* Converted total pixel count to square kilometers using the 10m $\times$ 10m spatial resolution ($1 \text{ Pixel} = 100 \text{ m}^2$).

### Step 5: Advanced Cartographic Visualization
* Designed a multi-page publication-grade layout using **QGIS Print Layout**.
* Implemented **Inverted Polygon Masking** to focus visual attention strictly within the district boundary.
* Integrated dynamic **HTML/CSS-rendered widgets** for statistical reporting, technical metadata, and visual consistency.
* Applied specialized thematic color palettes:
  * **2024 Baseline Map:** Hot Magenta / Pink (`#D946EF`) for high-contrast disaster baseline mapping.
  * **2025 Comparative Map:** Cyan / Ocean Blue (`#0284c7`) to symbolize drainage and recovery.

---

## 📁 Repository Structure

```text
📦 Barpeta-Flood-Analysis-2024-2025
 ┣ 📂 docs/               # High-resolution PDF reports & exported maps (PNG/JPG)
 ┣ 📂 scripts/            # QGIS Raster Calculator formulas & HTML card snippets
 ┣ 📂 layout_templates/   # QGIS Print Layout templates (.qpt)
 ┣ 📜 README.md           # Project documentation
 ┗ 📜 LICENSE             # Open-source license (MIT/GPL)
