#import OGR
import csv


#dirtosave = "E:/UW Lab jobs/7. Elevation adaption of Pheasants/IUCNbirds/Mitogenomespp/"
#birds_layer = QgsVectorLayer("E:/UW Lab jobs/7. Elevation adaption of Pheasants/IUCNbirds/IUCNbirds.shp", "IUCN_birds", "ogr")
#if not birds_layer.isValid:
#    print("failed to load")

with open('E:/UW Lab jobs/7. Elevation adaption of Pheasants/IUCNbirds/Spplist_color_pattern.csv') as csvDataFile:
    spplist = csv.DictReader(csvDataFile)
    for row in spplist:
        print("starting finding")
        birds = iface.activeLayer()
        spp = row['spclist']
        print(spp)
        exprstring = "\"SCINAME\"=" +"\'" + spp + "\'"
        print(exprstring)
        expr = QgsExpression( exprstring )
        it = birds.getFeatures( QgsFeatureRequest( expr ) )
        ids = [i.id() for i in it]
        print(ids)
        birds.setSelectedFeatures( ids )
        res = QgsVectorFileWriter.writeAsVectorFormat( birds,
                dirtosave + spp + ".shp",
                'System',
                None, #crs
                'ESRI Shapefile',
                True #onlySelected
                )
        if res != QgsVectorFileWriter.NoError:
            print ('writing Error number:')
        else:
            print ("writing Done!")
            print(spp + "done \n")