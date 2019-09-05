#Notandi slær inn tölu. Ef talan er minni en 0 þá hættir 
#forritið að keyra. Ef talan er stærri en 0 fer forritið
#í While-lykkju þar sem notandinn slær inn fleiri tölur,
#eina í einu. Lykkjan heldur áfram að keyra þar til slegin
#er inn tala sem er 0 eða minni. Þá ber forritið saman
#tölurnar sem notandinn slær inn og prentar hæstu.

num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0

while num_int > 0:
  num_int = int(input("Input a number: "))
  
  if num_int > max_int:
    max_int = num_int

# Fill in the missing code
print("The maximum is", max_int)    # Do not change this line

 
