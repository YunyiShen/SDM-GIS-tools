import processing
import glob
dir = "E:\\UW Lab jobs\\7. Elevation adaption of Pheasants\\IUCNbirds\\Mitogenomespp\\Polygon"
dir_save = "E:\\UW Lab jobs\\7. Elevation adaption of Pheasants\\IUCNbirds\\Mitogenomespp\\Rasters"
shps = glob.glob(dir+"\\*.shp")

#input = iface.activeLayer()
for polyg in shps:
    layer = QgsVectorLayer(polyg,"polygon","ogr")
    #extent = layer.extent()
    xmin = -180.0000
    xmax = 180.0000
    ymin = -90.0000
    ymax = 90.0000
    newfilename = polyg.replace(dir,dir_save)
    newfilename = newfilename.replace(".shp",".tif")
    print(newfilename)
    processing.run("gdal:rasterize", 
                    {"INPUT":layer,
                   "FIELD":"SEASONAL",
                   "DIMENSIONS":1,
                   "WIDTH":0.1,
                   "HEIGHT":0.1,
                   "UNITS":1,
                   "EXTENT":"%f,%f,%f,%f"% (xmin, xmax, ymin, ymax),
                   "TFW":1,
                   "RTYPE":1,
                   "NO_DATA":0,
                   "COMPRESS":0,
                   "JPEGCOMPRESSION":1,
                   "ZLEVEL":1,
                   "PREDICTOR":1,
                   "TILED":False,
                   "BIGTIFF":2,
                   "EXTRA": '',
                   "OUTPUT":newfilename})