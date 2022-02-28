def search(li, low, high, key):
    if low > high:
        return False

    mid = int((low + high) / 2)
    if li[mid] == key:
        return mid

    if li[low] <= li[mid]:

        if key >= li[low] and key <= li[mid]:
            return search(li, low, mid-1, key)
        return search(li, mid + 1, high, key)

    if key >= li[mid] and key <= li[high]:
        return search(li, mid + 1, high, key)
    return search(li, low, mid-1, key)


li = []
try:
    [li.append(int(x)) for x in input('nums with spaces between ').split()]
    li = sorted(li)
except:
    print('This is not all numbers')
key = int(input('find '))

i = search(li, 0, len(li)-1, key)
if i != False:
    print(f"Index: {i}")
else:
    print("Key not found")
