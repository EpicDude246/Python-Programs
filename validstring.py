string = input('string ')
openingBrackets = ['{', '[', '(']
closingBrackets = ['}', ']', ')']
brackets = {')': '(', '}': '{', ']': '['}
stack = []

for item in string:
    if item in openingBrackets:
        stack.append(item)
    elif item in closingBrackets:
        if len(stack) == 0:
            print(False)
            quit()
        if stack[-1] == brackets[item]:
            stack.pop()
        else:
            print(False)
            quit()
print(True)
