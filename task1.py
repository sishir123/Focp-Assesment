print("------------------------------------------------------------------------\n")
print("Stop! Who would cross the Bridge of Death")
print("Must answer me these questions three, 'ere the other side he see.\n")

Entry=input("Enter your name:\n")

if("Arthur" in Entry): #Check whether the input is Arthur or not.
    correct= True           
    if(correct):
        print("My liege! You may pass!")
else:
    Hello=input("What is your quest:\n") #Ask the question if the user says grail or not
    if ("Grail" in Hello)|("grail" in Hello):
            color=input("What is your favorite colour?\n") #Ask the favorite colour
            if (color[0]==Entry[0]):
                print("You may pass!")
            else:
                print("Incorrect! You must now face the Gorge of Eternal Peril.")
    else:
        print("Only those who seek the Grail may pass.")