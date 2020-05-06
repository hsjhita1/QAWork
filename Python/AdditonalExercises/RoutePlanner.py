peakList = [0, 8, 4, 12, 2, 10, 6, 12, 1, 9, 5, 12, 3, 11, 7, 15]

def findRoute(peaks):
    routeList = []
    route = []
    for i in range(len(peaks)):
        if i == 0:
            routeList.append(peaks[i])
        elif routeList[i-1] < peaks[i]:
            routeList.append(peaks[i])
        elif routeList[i-1] > peaks[i]:
            routeList.append(peaks[i-1])

    for i in range(len(routeList)):
        if i == 0:
            route.append(routeList[i])
        elif routeList[i] not in (route):
            route.append(routeList[i])
    return route

print(findRoute(peakList))