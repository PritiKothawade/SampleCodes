def findDup(IntList):
    countList = []
    dupList = []
    for i in range(0,len(IntList)):
        countList.append(0)
    for val in IntList:
        countList[val-1] += 1
    for i in range(len(countList)):
        if countList[i] > 1:
            dupList.append(i+1)
    return dupList


def find_dupl(IntList):
    dupList  = []
    for i in IntList:
        if IntList[abs(i)] > 0:
            IntList[abs(i)] = IntList[abs(i)]*-1
            print(IntList)
        else:
            dupList.append(i)
        print(dupList)
    return dupList


if __name__ == "__main__":
    print(find_dupl([1,2,1,3,1,2]))