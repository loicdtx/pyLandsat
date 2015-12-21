from osgeo import gdal
from pymodis import downmodis
import glob

dest = "/home/dutri001/sandbox/MODIS/"
tiles = "h18v03"
day = "2015.11.18"
enddate = "2015.11.16"
product = "MOD13A2.006"


modis_down = downmodis.downModis(destinationFolder=dest, tiles=tiles, today=day, enddate=enddate, product=product)
modis_down.connect()
modis_down.downloadsAllDay()

# List files with the hdf extension
MODIS_file = glob.glob(dest + '*.hdf')

# 
sds = gdal.Open(MODIS_file[0]).GetSubDatasets()
vi = gdal.Open(sds[0][0])
vi_np = vi.ReadAsArray()
print vi_np




