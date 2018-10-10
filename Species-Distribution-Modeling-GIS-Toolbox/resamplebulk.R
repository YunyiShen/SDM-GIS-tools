require(raster)
setwd('H:/rasters')
file = list.files(pattern = 'tif')

dirsave = 'H:/rasters/asc/'

templ = raster(file[1])
tempres = templ
res(tempres) = 10000

templ = resample(templ,tempres) 
plot(templ)

rm(tempres)

for (i in 1 : length(file)){
  temp = raster(file[i])
  temp = resample(temp , templ)
  
  #filenum = substr(file[i],start = 8,stop = nchar(file[i]))
  #dir = paste0(dirsave,'CHELSA_bio_',filenum)
  
  dir = paste0(dirsave,filenamet,'.asc')
  print(dir)
  writeRaster(temp,dir)
  rm(temp)
  
}
