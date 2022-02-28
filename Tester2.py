letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', ':', '/']

def encrypt(str, n):
    result = []
    for x in str:
        if x == " ":
            converted = " "
            result.append(converted)
        else:
            converted = (letters.index(x) + n) % 29
            result.append(letters[converted])
    final = ''.join(result)
    return final


def decrypt(str, n):
    result = []
    for i in str:
        if i == " ":
            converted = " "
            result.append(converted)
        else:
            converted = (letters.index(i) - n) % 29
            result.append(letters[converted])
    final = ''.join(result)
    return final

print(encrypt('https://theannoyingsite.com/', 5))
print(decrypt(encrypt('https://theannoyingsite.com/', 5), 5))