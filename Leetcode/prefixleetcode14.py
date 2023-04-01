#Returns the longest common prefix in all of the members of the list "strs"

strs = ["run", "runt", "rupo"]
prefix = ''
try:
    for i in range(len(strs[0])):
        x = strs[0][i]
        test = True
        for j in range(len(strs)):
            if strs[j][i] != strs[0][i]:
                test = False
        if test:
            prefix = prefix + x
        else:
            raise

except:
    pass

finally:
    print(prefix)
    


