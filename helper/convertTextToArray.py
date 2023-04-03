def convertTextToArray(testFile: str) -> list:
    txtCoordinates = open(testFile, 'r', encoding='utf-8').read()

    listCoordinates = txtCoordinates.split('\n')

    listOrderedCoordinates = []
    for coord in listCoordinates:
        listCoord = coord.split(',')
        listOrderedCoordinates.append(listCoord)

    return listOrderedCoordinates
