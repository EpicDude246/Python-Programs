def common(list1, list2): 
    result = False
    for x in list1: 
        for y in list2: 
            if x == y: 
                result = True
                return result  
                  
    return result
def listy():
    list2 = []
    l = 0
    while l != "NOMORE":
        l = input("Num: NOMORE for no more items in list ")
        list2.append(l)
        if "NOMORE" in list2:
            list2.remove("NOMORE")
    return list2
list1 = listy()
list2 = listy()
print(common(list1, list2))