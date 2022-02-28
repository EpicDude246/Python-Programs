def signature(word):
  word = word.lower()
 
  if len(word) <= 3:
    return word
    
  middle = list(word[1:-1])
  return word[0] + ''.join(sorted(middle)) + word[-1]
  
signature("Welcome") # 'wcelmoe'
signature("Woclmee") # 'wcelmoe'

handler = open("english.txt", encoding = "utf-8")
words = [word.strip() for word in handler.readlines()]
handler.close()
  
# Load dictionary entries
dictionary = {signature(word):word for word in words}

def unshuffle_one(word):
  sig = signature(word)
  return dictionary[sig] if sig in dictionary else word
    
def unrepl(match):
  return unshuffle_one(match.groups()[0])
  
def unshuffle(text):
  return re.sub("(\w+)", unrepl, text)
  
print(unshuffle("The eofrft rreuqied to sfssllcceuuy dhiepecr sbecmrald "
                "pgsaases daiaarclltmy ianserecs as wdors get lehegtinr."))