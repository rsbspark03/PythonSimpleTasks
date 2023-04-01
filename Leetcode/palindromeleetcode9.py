#Checks if integer "x" is a palindrome

x = 1234567899987654321
if (len(str(x)) % 2) == 1:
    y = str(x)

    #print(y[:int((len(y)-1)/2)])
    #print(y[:int((len(y)-1)/2):-1])
    if y[:int((len(y)-1)/2)] == y[:int((len(y)-1)/2):-1]:
        print('True')
    else:
        print('False')

else:
    y = str(x)
    #print(y[:int(len(y)/2)])
    #print(y[:int(len(y)/2)-1:-1])
    if y[:int(len(y)/2)] == y[:int(len(y)/2)-1:-1]:
        print('True')
    else:
        print('False')
