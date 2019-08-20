#Name: Cymmone Yancey
#Date: 07/03/19
#Description: Random number generator, modulus, conditional 
#             statememnts and while loops are utilized to make a
#             guessing game where the user states if the secret
#             number is even or odd.

from random import randint

secret_num = randint(0,9)
num = int(secret_num + 1)
determine = int(num %2)
num_type = str("")

uIn = str(raw_input("Guess if the number is even or odd: "))

if determine == 0:
   num_type = "even"
else :
   num_type = "odd"
   
if num_type == uIn:
   print("Congratulations, you guessed correctly :)!" 
          +"\nThe number was " +str(num))
elif num_type != uIn:
   print("Congratulations, you were wrong :(!"
          +"\nThe number was " +str(num))
   again = str(raw_input("Would you like to try again, y or n? "))
   while (again == "y"):
      uIn = str(raw_input("Guess if the number is even or odd: "))
      
      if determine == 0:
         num_type = "even"
      else :
         num_type = "odd"
         
      if num_type == uIn:
         print("Congratulations, you guessed correctly :)!" 
                +"\nThe number was " +str(num))
         again = "n"
      elif num_type != uIn:
         print("Congratulations, you were wrong :(!"
                +"\nThe number was " +str(num))
         again = str(raw_input("Would you like to try again, y or n? "))

      






