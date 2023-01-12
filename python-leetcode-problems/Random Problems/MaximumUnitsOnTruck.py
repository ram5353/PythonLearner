def maximumUnits(boxTypes, truckSize):
        max_capacity = 0
        boxTypes.sort(key= lambda x: -x[1])
        for box, units in boxTypes:
            if truckSize >= box:
                truckSize -= box
                max_capacity += box * units
            else:
                max_capacity += truckSize * units
                break

        return max_capacity

print(maximumUnits([[1,3],[2,2],[3,1]], 4))