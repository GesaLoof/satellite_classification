
import ee
import geemap
import os
from datetime import datetime

class SatelliteImageCollector:
    def __init__(self):
        # Initialize Earth Engine
        try:
            ee.Initialize()
        except Exception as e:
            ee.Authenticate()
            ee.Initialize()
    
    def download_satellite_images(self, 
                                region_of_interest,
                                start_date,
                                end_date,
                                output_folder,
                                collection="LANDSAT/LC08/C02/T1_L2"):
        """
        Download satellite images for a specific region and time period
        
        Args:
            region_of_interest: ee.Geometry object defining the area
            start_date: Start date in 'YYYY-MM-DD' format
            end_date: End date in 'YYYY-MM-DD' format
            output_folder: Path to save the downloaded images
            collection: Name of the GEE collection to use
        """
        # Create the image collection
        image_collection = (ee.ImageCollection(collection)
                          .filterBounds(region_of_interest)
                          .filterDate(start_date, end_date))
        
        # Create output directory if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)
        
        # Get the image list
        image_list = image_collection.toList(image_collection.size())
        
        # Download each image
        for i in range(image_collection.size().getInfo()):
            image = ee.Image(image_list.get(i))
            
            # Get the date of the image
            date = ee.Date(image.get('system:time_start')).format('YYYY-MM-dd').getInfo()
            
            # Export the image
            geemap.ee_export_image(
                image,
                filename=os.path.join(output_folder, f"satellite_image_{date}.tif"),
                scale=30,
                region=region_of_interest,
                file_per_band=False
            )

    def get_rectangle_region(self, min_lon, min_lat, max_lon, max_lat):
        """
        Create a rectangular region of interest
        
        Args:
            min_lon: Minimum longitude
            min_lat: Minimum latitude
            max_lon: Maximum longitude
            max_lat: Maximum latitude
        
        Returns:
            ee.Geometry.Rectangle object
        """
        return ee.Geometry.Rectangle([min_lon, min_lat, max_lon, max_lat])

# Example usage
collector = SatelliteImageCollector()

# Define region of interest (example: part of San Francisco)
roi = collector.get_rectangle_region(
    min_lon=-122.5,
    min_lat=37.7,
    max_lon=-122.4,
    max_lat=37.8
)

# Download images
collector.download_satellite_images(
    region_of_interest=roi,
    start_date='2023-01-01',
    end_date='2023-12-31',
    output_folder='satellite_images'
)
