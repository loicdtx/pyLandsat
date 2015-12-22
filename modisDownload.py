from osgeo import gdal
from pymodis import downmodis
import glob
import numpy as np

import matplotlib.pyplot as plt


# Variables for data download
dest = "/home/dutri001/sandbox/MODIS/"
tiles = "h18v03"
day = "2015.11.18"
enddate = "2015.11.16"
product = "MOD13A2.006"

# Init download class, connect and download
modis_down = downmodis.downModis(destinationFolder=dest, tiles=tiles, today=day, enddate=enddate, product=product)
modis_down.connect()
modis_down.downloadsAllDay()

# List files with the hdf extension
MODIS_file = glob.glob(dest + '*.hdf')

# Get subdatasets of the first file of the MODIS_file list
sds = gdal.Open(MODIS_file[0], gdal.GA_ReadOnly).GetSubDatasets()
print sds[0][0]
print sds[11][0]

# Open vi, to get the metadata (geoTransform, dimensions, projection)
vi = gdal.Open(sds[0][0])
ind = [1, 11]
# vi_np = np.zeros((vi.RasterYSize, vi.RasterXSize, 2), np.int16)
# Allocate zeros array of desired size
vi_np_sub = np.zeros((200, 200, 2), np.int16)
# Read data in array
for i in range(len(ind)):
	src = gdal.Open(sds[ind[i]][0])
	vi_np_sub[:,:,i] = src.ReadAsArray(400, 400, 200, 200)

# Perform value replacement and drop QA layer
vi_np_sub[vi_np_sub[:,:,1] > 1, 0] = -3000
vi_np_out = vi_np_sub[:,:,0]
# Drop second dimension of array


print vi_np_sub.shape
print vi.GetGeoTransform()

plt.imshow(vi_np_out)
plt.show()

# Get Geotransforms of original dataset (vi.GetGeoTransform())
# Modify the list of geotransforms according to the array subset
# Set modified GeoTransform to new dataset
# See http://gis.stackexchange.com/questions/58517/python-gdal-save-array-as-raster-with-projection-from-other-file




# driver = gdal.GetDriverByName('ENVI')
# driver.Register()
# outDataset = driver.Create('ERS1PRI_19920430_ENVI_subset', 50, 50, 1, gdal.GDT_Float32) 


# outBand = outDataset.GetRasterBand(1)
# outBand.WriteArray(subset, 0, 0)
# band = None
# dataset = None
# outDataset = None
# subset = None














