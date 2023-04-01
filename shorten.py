

user = input("Enter string: ")
#print(len(user))
default = ["a", "e", "i", "o", "u", " "]

test = user.split()
#print(test)
for i in range(len(test)):
    if len(test[i]) > 3:
        test[i] = test[i][0:3]

type2 = ' '.join(test)
print(type2)

for i in default:
    new = user.replace(i, "")
    user = new

print(user)