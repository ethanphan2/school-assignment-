import time

artifact = False

print("Anti-Gravity Adventure")
time.sleep (0.5)
print("Level one")
time.sleep (0.5)
print("You wake up stranded on a ship.")
time.sleep (1)
name = input("Your name is: ")
print(name,"wakes up in an unknown spaceship. A mysterious artifact lies on the ground.")
time.sleep (3)
print("Does",name,"...")
time.sleep (0.5)
print("A. Examine the artifact")
time.sleep (0.5)
print("B. Try to find an exit")
time.sleep (1)
answer = input("Answer:")

if answer == ("A"):
    time.sleep (0.5)
    print ("artifact starts moving and glowing then stops")
    time.sleep (0.5)
    print ("does" , name , "...")
    time.sleep (0.5)
    print("A.toss artifact away")
    time.sleep (0.5)
    print ("B.keep it for later")
    time.sleep (0.5)
    answer = input ("answar: ")

    if answer == "A" :
        time.sleep (0.5)
        print ("you toss the artifact away but it suddenly combusts melting all the flesh of your bones")
        time.sleep (0.5)
        print ("YOU DIED")

    if answer == "B" :
        time.sleep (0.5)
        print (name," decided to keep the artifact for later")
        time.sleep (1)
        print ("[ARTIFACT OBTAINED]")
        artifact = True

if answer == "B" or artifact == True:
    time.sleep (0.5)
    print (name,"decided to wander the halls")
    time.sleep (0.5)
    
        
        

