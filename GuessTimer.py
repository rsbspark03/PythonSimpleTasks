import time
from matplotlib import pyplot as np
import getpass

% A game where the User enters a string "password" and then enters the time allowed to guess. 
% Then after a countdown, the User gets the specified amount of time to guess the word. 

password = getpass.getpass('Password:')
t = float(input("Enter allowed time for guesser: "))
print("3!")
time.sleep(1)
print("2!")
time.sleep(1)
print("1!")
time.sleep(1)
print("Start guessing!!")
start = time.time()
end = time.time()

while True:
    #print("{}".format(end-start))
    #print("{}".format(end))

    a = input("Enter password: ")
    end = time.time()
    print("Time left: {}".format(int(t-(end-start))))

    if (end - start) > t:
        print("You ran out of time")
        break

    elif a == password:
        print("Correct!!!")
        break

    else:
        print("Wrong password")
        pass


