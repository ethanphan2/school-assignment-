import random 

playerhp = int (1000)
alienhp = int (1000) 
playeralive = True
alienalive = True
bullets = int (3)

name = "jota" 


print (name , "encounters a weird being")
print (" does",name,"...")
print ("A. fight")
print ("B. run away")
answer = input ("answer... :")

if answer == "A" or "a":
  print ("[COMMENCING BATTLE]")
  print (name , "VS Alien")

  while playeralive == True and alienalive == True:
    print ("does" ,  name , "...")
    print ("A. heavy attack")
    print ("B. light attack")
    print ("C.gun attack [ you have",bullets,"bullets]")
    answera = input ("answer: ")


    if answera == "A":
      print (name , "went for a heavy attack!!")
      dmg = random.randint(70,100)
      alienhp = alienhp - dmg

      print (name , "did" , dmg ,"damage to the alien!! it now has " , alienhp)

      aliendmg = random.randint (80 , 150)

      playerhp = playerhp - aliendmg
      print ("the alien fought back and did" , aliendmg , "damage!!" , name , "now has" ,playerhp, "health")

    elif answera == "B":
        print (name , "went for a light attack!!!")
        dmg = random.randint (50 , 80)
        print (name , "did" , dmg ,"damage to the alien!! it now has " , alienhp)
        aliendmg = random.randint (80 , 150)
        playerhp = playerhp - aliendmg
        print ("the alien fought back and did" , aliendmg , "damage!!" , name , "now has" ,playerhp, "health")

    elif answera == "C":
        if bullets > 0:
            print (name , "went for a gun attack!!!")
            bullets = bullets - 1
            dmg = random.randint (1 , 1000)
            print ("you used one bullet , you now have" ,bullets,"bullets")
            alienhp = alienhp - dmg
            print (name , "did" , dmg ,"damage to the alien!! it now has " , alienhp)
            aliendmg = random.randint (80 , 150)
            playerhp = playerhp - aliendmg
            print ("the alien fought back and did" , aliendmg , "damage!!" , name , "now has" ,playerhp, "health")
        else :
            print ("you have no more bullets!!!")
    if playerhp <= 0:
        playeralive = False

    if alienhp <= 0:
        alienalive = False
    

    
        
        
