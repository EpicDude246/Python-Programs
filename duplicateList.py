def Remove(duplicate): 
    list1 = [] 
    for num in duplicate: 
        if num not in list1: 
            list1.append(num) 
    return list1
def listy():
    list2 = []
    l = 0
    while l != "NOMORE":
        l = input("Num: NOMORE for no more items in list ")
	l.remove("NOMORE")
        list2.append(l)
    return list2
    
listt = listy()
print(Remove(listt)) 