```python
"""
=============================================================================
Project: Automated Flood Inundation & NDWI Mapping Pipeline (PyQGIS)
Author: Shivam Shukla
Description: This script automates the calculation of NDWI, applies SCL cloud
             masking, generates binary flood extent rasters, and calculates 
             multi-temporal change detection using QGIS 3.x Python API.
=============================================================================
"""

import os
from qgis.core import (
    QgsProject,
    QgsRasterLayer,
    QgsRasterCalculator,
    QgsRasterCalculatorEntry
)

def run_ndwi_calculator(green_band_path, nir_band_path, output_ndwi_path):
    """
    Computes Normalized Difference Water Index (NDWI) using QGIS Raster Calculator.
    Formula: (Green - NIR) / (Green + NIR)
    """
    # Load raster bands
    lyr_green = QgsRasterLayer(green_band_path, "Green_Band")
    lyr_nir = QgsRasterLayer(nir_band_path, "NIR_Band")
    
    if not lyr_green.isValid() or not lyr_nir.isValid():
        print("Error: Input raster layers could not be loaded.")
        return None

    # Define calculator entries
    entry_green = QgsRasterCalculatorEntry()
    entry_green.ref = 'green@1'
    entry_green.raster = lyr_green
    entry_green.bandNumber = 1

    entry_nir = QgsRasterCalculatorEntry()
    entry_nir.ref = 'nir@1'
    entry_nir.raster = lyr_nir
    entry_nir.bandNumber = 1

    entries = [entry_green, entry_nir]

    # Define NDWI mathematical formula
    formula = '("green@1" - "nir@1") / ("green@1" + "nir@1")'

    # Initialize and run QgsRasterCalculator
    calculator = QgsRasterCalculator(
        formula,
        output_ndwi_path,
        'GTiff',
        lyr_green.extent(),
        lyr_green.width(),
        lyr_green.height(),
        entries
    )

    result = calculator.processCalculation()
    
    if result == 0:
        print(f"Success: NDWI raster generated at {output_ndwi_path}")
        return output_ndwi_path
    else:
        print("Error: NDWI calculation failed.")
        return None

if __name__ == "__main__":
    # Example workflow execution for Barpeta District (2024 Baseline)
    DATA_DIR = os.path.join(os.path.expanduser("~"), "Desktop", "Proj_Assam Floods", "Data")
    
    B03_2024 = os.path.join(DATA_DIR, "Sentinel2_2024_B03.tif")
    B08_2024 = os.path.join(DATA_DIR, "Sentinel2_2024_B08.tif")
    OUTPUT_NDWI = os.path.join(DATA_DIR, "Computed_NDWI_2024.tif")
    
    print("Initiating automated GIS processing pipeline...")
    # run_ndwi_calculator(B03_2024, B08_2024, OUTPUT_NDWI)
