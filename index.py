from helper.convertTextToArray import convertTextToArray
import utm

fileContent = convertTextToArray('filemc.txt')
geoLocations = []

for coordinate in fileContent:
    easting = float(coordinate[0])
    northing = float(coordinate[1])
    zoneNumber = int(coordinate[2])
    zoneLetter = coordinate[3]
    convertedCoord = utm.to_latlon(easting, northing, zoneNumber, zoneLetter)
    geoLocations.append(convertedCoord)
    print(geoLocations[0][0])


