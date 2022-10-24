
print("Welcome To The Simple IT Quiz Game !! ")

playing_status=input("Do You Want To Play This Game? " + "" + "(Yes/No)\n").lower()

if playing_status != "yes":
  exit()
else:
  name= input("What Is Your Name?\n")
print("Ok " + name +","+ " Let's Start !!\n")

score = 0

answer=input("What Is CPU stands for?\n").lower()
if answer == "central processing unit":
  print("Correct\n")
  score += 1
else:
  print("Incorrect")

answer=input("What Is GPU stands for?\n").lower()
if answer == "graphics processing unit":
  print("Correct\n")
  score += 1
else:
  print("Incorrect\n")

answer=input("What is PSU stands for?\n").lower()
if answer == "power supply unit":
  print("Correct\n")
  score += 1
else:
  print("Incorrect\n")

answer=input("What is RAM stands for?\n").lower()
if answer == "random access memory":
  print("Correct\n")
  score += 1
else:
  print("Incorrect\n")

print("(Yes or No)\n")

answer=input("Is RAM a Volatile memory?\n").lower()
if answer == "yes":
  print("Correct\n")
  score += 1
else:
  print("Incorrect\n")

answer=input("Is Hard Disk a Volatile memory?\n").lower()
if answer == "no":
  print("Correct\n")
  score += 1
else:
  print("Incorrect\n")

answer=input("Is Cache memory a Volatile memory?\n").lower()
if answer == "yes":
  print("Correct\n")
  score += 1
else:
  print("Incorrect\n")

answer=input("Should we pay for using OS X?\n").lower()
if answer == "yes":
  print("Correct\n")
  score += 1
else:
  print("Incorrect\n")

answer=input("Is Windows open source?\n").lower()
if answer == "no":
  print("Correct\n")
  score += 1
else:
  print("Incorrect\n")

answer=input("Is Ubuntu a linux Distro?\n").lower()
if answer == "yes":
  print("Correct\n")
  score += 1
else:
  print("Incorrect\n")

print("You Completed The Quiz!!" + " Here Are The Results..\n" )
print("You got " + str(score)+ " questions correct!" + " Your score is " + str(score/10 *100) + "%...")


