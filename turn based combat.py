import random 

playerhp = int (1000)
alienhp = int (1000) 
playeralive = (True)
alienalive = (True)

print (name , "encounters a weird being")
print (" does",name,"...")
print ("A. fight")
print ("B. run away")
answer = input ("answer... :")

if answer == "A" or "a":
  print ("[COMMENCING BATTLE]")
  print (name , "VS Alien")

  while playeralive == True and alienalive == True:
    print ("does" name , "...")
    print ("A. heavy attack")
    print ("B. light attack")
    print ("C.gun attack")
