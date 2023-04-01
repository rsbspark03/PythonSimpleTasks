x = "([]())"
queue = []
brackets = {
    ')' : '(',
    ']' : '[',
    '}' : '{'
}

for char in x:
    if char == '(' or char == '[' or char == '{':
        queue.append(char)
        #print(queue)
    else:
        #print(brackets[char])
        if len(queue) == 0:
            print("False")
            exit()

        elif brackets[char] == queue[-1]:
            queue.pop()
            continue

        else:
            print('False')
            exit()
print('True')