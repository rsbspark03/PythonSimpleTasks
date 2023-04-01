rno = "LXII"
dno = 0
i = 0
lets = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}   

while i < len(rno):
    #print(rno[i])
    if i == len(rno) - 1:
        #print("1")
        dno += lets[rno[i]]
        i += 1
    elif lets[rno[i]] >= lets[rno[i+1]]:
        #print("2")
        dno += lets[rno[i]]
        i += 1
    else:
        #print("3")
        dno += lets[rno[i+1]] - lets[rno[i]]
        i += 2

print(dno)
