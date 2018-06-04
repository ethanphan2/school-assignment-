import time
import random

artifact = False

playerhp = int (1000)
alienhp = int (1000)
playeralive = True
alienalive = True
bullets = int (3)

print("Anti-Gravity Adventure")
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

if answer == "A":
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
    print (name , "hears growling coming from a hall")
    time.sleep (0.5)
    print ("does", name , "...")
    time.sleep (0.5)
    print ("A. investigate it")
    time.sleep (0.5)
    print ("B. run away")
    time.sleep (0.5)
    answer = input ("answer: ")

    if answer == "A":
        print ("you encounterd an alien")
        if artifact == False :
            print ("you got attacked by the alien and killed")
            time.sleep (0.5)
            print ("[YOU DIED]")
        elif artifact == True :
            print ("the alien tried to attack")
            time.sleep (0.5)
            print ("the artifact you had started glowing and the alien jumped back")
            time.sleep (0.5)
            print ("the alien tries to fight back")
            print (" does",name,"...")
            print ("A. fight")
            print ("B. run away")
            answer = input ("answer... :")

            if answer == "A" or "a":
              print ("[COMMENCING BATTLE]")
              print (name , "VS Alien")

              while playeralive == True and alienalive == True:
                time.sleep (0.5)
                print ("does" ,  name , "...")
                time.sleep (0.5)
                print ("A. heavy attack")
                time.sleep (0.5)
                print ("B. light attack")
                time.sleep (0.5)
                print ("C.gun attack [ you have",bullets,"bullets]")
                time.sleep (0.5)
                answera = input ("answer: ")


                if answera == "A":
                  time.sleep (0.5)
                  print (name , "went for a heavy attack!!")
                  dmg = random.randint(70,100)
                  alienhp = alienhp - dmg
                  time.sleep (0.5)

                  print (name , "did" , dmg ,"damage to the alien!! it now has " , alienhp)

                  aliendmg = random.randint (80 , 150)

                  playerhp = playerhp - aliendmg
                  time.sleep (0.5)
                  print ("the alien fought back and did" , aliendmg , "damage!!" , name , "now has" ,playerhp, "health")

                elif answera == "B":
                    time.sleep (0.5)
                    print (name , "went for a light attack!!!")
                    dmg = random.randint (50 , 80)
                    alienhp = alienhp - dmg
                    time.sleep (0.5)
                    print (name , "did" , dmg ,"damage to the alien!! it now has " , alienhp)
                    aliendmg = random.randint (80 , 150)
                    playerhp = playerhp - aliendmg
                    time.sleep (0.5)
                    print ("the alien fought back and did" , aliendmg , "damage!!" , name , "now has" ,playerhp, "health")

                elif answera == "C":
                    if bullets > 0:
                        time.sleep (0.5)
                        print (name , "went for a gun attack!!!")
                        bullets = bullets - 1
                        dmg = random.randint (1 , 1000)
                        time.sleep (0.5)
                        print ("you used one bullet , you now have" ,bullets,"bullets")
                        alienhp = alienhp - dmg
                        time.sleep (0.5)
                        print (name , "did" , dmg ,"damage to the alien!! it now has " , alienhp)
                        aliendmg = random.randint (80 , 150)
                        playerhp = playerhp - aliendmg
                        time.sleep (0.5)
                        print ("the alien fought back and did" , aliendmg , "damage!!" , name , "now has" ,playerhp, "health")
                    else :
                        time.sleep (0.5)
                        print ("you have no more bullets!!!")
                if playerhp <= 0:
                          time.sleep (0.5)
                          print ("you died")
                          time.sleep (0.5)
                          print ("try again?")
                          time.sleep (0.5)
                          print ("A. yes")
                          time.sleep (0.5)
                          print ("B. no ")
                          time.sleep (0.5)
                          retry = input ("answer: ")

                          if retry == "A":
                              playerhp = int (1000)


                          if retry == "B":
                              playeralive = False

                if alienhp <= 0:
                    alienalive = False
                    time.sleep (1)
                    print ("the alien screeches and runs away")
                    time.sleep (1)
                    print (name , "walks around a little more , and encountered an escape pod")
                    time.sleep (1)
                    print (name , "leaves the ship")
                    
    if answer == "B":
        time.sleep (0.5)
        print ("you tried to run away but the alien caught up and clawed your face off")
        time.sleep (0.5)
        print ("YOU DIED")
        
        
