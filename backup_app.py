
#import dependencies
import time
from PIL import Image    
from playsound import playsound  
import     sys        
from threading import Timer      
import os                                                      
import random
import pandas as pd




def escape_house_of_mirrors():
    #set the number of strikes(mistakes) the user is allowed to 0. So we can count them
    strikes = 0
    #user gets a random number of chances between 3 and 5
    chances = random.randrange(3,5)
    #list of rows-indexing starts at 0
    rows = [0,1,2,3]
    #list of columns 
    columns = ['a', 'b', 'c', 'd']
    #create a dataframe which will function as our scoreboard
    df = pd.DataFrame(rows,columns)
    while True:

        #we want to users starting y position to be between 0 and 3
        starting_y_axis = random.randrange(0,4)
        #we want the starting y position to be a value in list [columns ]
        starting_x_axis = random.choice(columns)
        #concatonate together, convert into to str
        starting_position = starting_x_axis + str(starting_y_axis)
         #create random exit position
        #we want to users starting y position to be between 0 and 3
        exit_y_axis = random.randrange(0,4)
        #we want the starting y position to be a value in list [columns ]
        exit_x_axis = random.choice(columns)
        #concatonate together, convert into to str
        exit_position = starting_x_axis + str(starting_y_axis)
        if starting_position!=exit_position:
            break
        else:
            pass




    #print how lucky the user is.
    print(f"You get {chances} chances to make it out alive")
    print('in the darkness, youre not sure where to do.')
    print(f"Your starting position is {starting_position}")
    print(f"your exit position is {exit_position}")








#helper function for using timer
def time_ran_out():
    print("You couldnt avoid the axe")
    time.sleep(5)
    #flush after every print because otherwise the terminal does not update real time
    sys.stdout.flush()
    #open image signifiying the player died
    img = Image.open(r'C:\Users\Gabriel Hernandez\Desktop\word_game\images\headless.png')
    img.show()
    #exit the terminal because the game is over
    os._exit(0)
    
   






#into function when the game starts
def into():
    #play intro music
    playsound(r'C:\Users\Gabriel Hernandez\Desktop\word_game\audio\Goosebumps_theme.mp3', False)
    #time the terminal to the music
    time.sleep(1)
    print("Welcome to Horrorland.")
    #flush after every print because otherwise the terminal does not update real time
    sys.stdout.flush()
    #time the terminal to the music
    time.sleep(2)
    print("Your choices will either keep you alive, or will lead to your demise.")
    #flush after every print because otherwise the terminal does not update real time
    sys.stdout.flush()
    #time the terminal to the music
    time.sleep(2)
    print("Choose wisely.")
    #flush after every print because otherwise the terminal does not update real time
    sys.stdout.flush()
    print(u"\u2620".encode('utf-8'))
    #flush after every print because otherwise the terminal does not update real time
    sys.stdout.flush()
    #time the terminal to the music
    time.sleep(3)

#entrance function , does the user want to play 
def park_entrance():
    print("You enter the abandonded carnival and are met by a ticket stand.")
    #flush after every print because otherwise the terminal does not update real time
    sys.stdout.flush()
    #time the terminal to the music
    time.sleep(3)
    print(" You slowly and cautiously approach the booth." )
    #flush after every print because otherwise the terminal does not update real time
    sys.stdout.flush()
    #time the terminal to the music
    time.sleep(3)
    print("No one is in the booth")
    #flush after every print because otherwise the terminal does not update real time
    sys.stdout.flush()
    #time the terminal to the music
    time.sleep(3)
    print('You stick your head in and shout hello! ')
    #flush after every print because otherwise the terminal does not update real time
    sys.stdout.flush()
    #time the terminal to the music
    time.sleep(3)
    #show image of the ticket attendant
    img = Image.open(r'C:\Users\Gabriel Hernandez\Desktop\word_game\images\attendant.png')
    img.show()
    #play the attendant welcome message
    playsound(r'C:\Users\Gabriel Hernandez\Desktop\word_game\audio\Welcome_to_horrorland.mp3')
    print('Admission is free. You"re our guest today.')
    #flush after every print because otherwise the terminal does not update real time
    sys.stdout.flush()
    #time the terminal to the music
    time.sleep(3)
    print("Do you wish to enter the park?\nPress 1 to continue.\nPress 2 to exit the park.")
    #flush after every print because otherwise the terminal does not update real time
    sys.stdout.flush()
    #user selects whether they want to enter the park or not
    entrance_selection = int(input('Enter your selection now:'))
    if entrance_selection == 1:
        #if they enter, play the enjoy message
        playsound(r'C:\Users\Gabriel Hernandez\Desktop\word_game\audio\Enjoy_horrorland.mp3')
    elif entrance_selection == 2:
        #if the dont enter, kill them
        print('You have nothing to fear, but fear itself.\n You have terminated the game\nSo we have terminated you\nGoodbye')
        #flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
        sys.exit('User bitched out')
    #catch any other selections
    else :
        print('The park paton has made a fatal error\n')
        #flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
#first ride. 
def guillotine_ride():
    print('After gathering your tickets, you see a large sign.')
    #flush after every print because otherwise the terminal does not update real time
    sys.stdout.flush()
    #time the terminal to the music
    time.sleep(2)
    print('The ride of your life, ')
    #flush after every print because otherwise the terminal does not update real time
    sys.stdout.flush()
    #time the terminal to the music
    time.sleep(1)
    print('You"ll never forget')
     #flush after every print because otherwise the terminal does not update real time
    sys.stdout.flush()
     #time the terminal to the music
    time.sleep(1)
    print('The ride name is Formula Guillotine ')
     #flush after every print because otherwise the terminal does not update real time
    sys.stdout.flush()
     #time the terminal to the music
    time.sleep(1)
    print('Guranteed to be a slicing good time')
    #flush after every print because otherwise the terminal does not update real time
    sys.stdout.flush()
    #time the terminal to the music
    time.sleep(2)
    #where does the user want to sit on the ride. This affects how much reaction time they get
    seat_selection = int(input("Where do you want to sit?: 1 for front, 2 for middle, 3 for rear."))
    #create a dictionary with the three user inputs
    seat_dic = {1 : "front", 2: "middle", 3: "rear"}
    #grab the value , based on the user key selection
    seat_choice = seat_dic[seat_selection]
    #F print where the user decided to get on the roller coaster
    print(f'You get into your seat at the {seat_choice} of the ride.')
    #flush after every print because otherwise the terminal does not update real time
    sys.stdout.flush()
    #play climbing roller coaster music
    playsound(r'C:\Users\Gabriel Hernandez\Desktop\word_game\audio\Climbing_the_coaster.mp3', False)
    #time the terminal to the music
    time.sleep(2)
    print("The cart starts to move.")
    #flush after every print because otherwise the terminal does not update real time
    sys.stdout.flush()
    #time the terminal to the music
    time.sleep(2)
    print('You"re pushed to the back of your seat')
    #flush after every print because otherwise the terminal does not update real time
    sys.stdout.flush()
    #time the terminal to the music
    time.sleep(2)
    print('You await what is at the top of the hill.')
    #flush after every print because otherwise the terminal does not update real time
    sys.stdout.flush()
    #time the terminal to the music
    time.sleep(5)
    print("You get higher and higher off the ground")
    #flush after every print because otherwise the terminal does not update real time
    sys.stdout.flush()
    #time the terminal to the music
    time.sleep(5)
    print('You squeeze the handle')
    #flush after every print because otherwise the terminal does not update real time
    sys.stdout.flush()
    #time the terminal to the music
    time.sleep(10)
    print('Your heart begins to race')
    #flush after every print because otherwise the terminal does not update real time
    sys.stdout.flush()
    #time the terminal to the music
    time.sleep(5)
    print('You finally reach the top')
    #flush after every print because otherwise the terminal does not update real time
    sys.stdout.flush()

    #show image at the top of the roller coaster
    img = Image.open(r'C:\Users\Gabriel Hernandez\Desktop\word_game\images\top_of_the_coaster.png')
    img.show()
    #play audio for the ride down
    playsound(r'C:\Users\Gabriel Hernandez\Desktop\word_game\audio\Descent_from_top.mp3')
    #based on user seat selection, their reaction time will be shorter at the front of the ride, longer at the rear.
    if seat_selection == 1:
        time_to_react = 3
    elif seat_selection ==2:
        time_to_react = 4
    elif seat_selection == 3:
        time_to_react = 5    
    else:
        #catch all other entries
        print('You did not secure yourself to the ride.\n Have fun falling to your death. \n Goodbye')
        
        sys.exit('User fell out of the ride')

    
    #call timer fuction, arguements are the users time_to_react(based on seat selection) and the time_ran_out function
    #the timer runs for anywhere from 3-5 seconds, and then calls the time_ran_out function of the user doesnt press a button
    t =Timer(time_to_react,time_ran_out)
    #start timer
    t.start()
    #prompt the user for input and quick
    user_input = input('Quick!\n Press any key.\n Better duck quick!\n Press Enter')
    #if the user managed to press a button
    if user_input!=None :
        
        print ('You managed to save your head by ducking')
        #flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
        #cancel the timer function and get out
        t.cancel()
    #if the user failed to input anything    
    elif user_input ==None :
        #call time_ran_out_function which kills the player and the game
   
        time_ran_out()
        
    else:
        print('You managed to crack your skull on a passing branch.\n Have fun falling unconcious and not waking up.\n Goodbye')
        #flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
        sys.exit('User hit their head')

#create functions for remaining parts of the story
def petting_zoo():
    print('petting zoo')







def house_of_mirrors():
    playsound(r'C:\Users\Gabriel Hernandez\Desktop\word_game\audio\House_of_mirrors.mp3')
    print("You enter the house of mirrors")
    print("You are presented with a choice")
    print('Right or Left?')
    eligible_choices = ['right', 'left', 'Right', 'Left', 'RIGHT', 'LEFT', 'R', 'L', 'r', 'l']
    while True:
        #grab user input as a string
    
        direction_choice = input('Make your choice: Right or Left')
        #check that user input matches a valid function in the function library
        if direction_choice  in eligible_choices:
            #pass the user input to the function dictionary, call the function based on which key was selected 
            print(f'Good Luck: You have chosen {direction_choice}')
            break
        else:
            #if input is invalid, stay in the loop and repeat the input function
            print('invalid selection:\n Please chose left or right.')
            
    left_choices = ['left','Left','LEFT','L','l']
    right_choices = ['right','Right','RIGHT','R', 'r']
    img = Image.open(r'C:\Users\Gabriel Hernandez\Desktop\word_game\images\in_the_hall_of_mirrors.png')
    img.show()
    time.sleep(5)
    print('You find yourself in a hall of mirrors.')
    print("You proceed into the unknown.")

    if direction_choice in left_choices:
        #scenario 1
        print('The door slams shut')
        time.sleep(5)
        print('The room is dark')
        time.sleep(5)
        playsound(r'C:\Users\Gabriel Hernandez\Desktop\word_game\audio\Where_are_you.mp3')
        print('You find yourself trapped in\n The room is dark. \n No one can hear your screams')
        time.sleep(5)
        img = Image.open(r'C:\Users\Gabriel Hernandez\Desktop\word_game\images\demon.png')
        img.show()
        print("You must make your selections carefully, or else you will trapped forever.")
    elif direction_choice in right_choices:
        #scenario 2
        print('scenario 2')
    else:
        print('You managed to get trapped and lost for eternity.\n Have fun screaming for days, and then starving to death.\n Goodbye')
        #flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
        sys.exit('User got lost and died.')




#create functions for remaining parts of the story
def shooting_gallery():
    print('shooting gallery')



#create a main menu where the user can choose which ride(function) they want to play
def park_map():
    print('Having survived your first ride')
    sys.stdout.flush()
    print('You look at a nearby map')
    #create dictionary of current functions 
    map_dic = {1: 'guillotine_ride', 2: 'petting_zoo', 3 :'shooting_gallery', 4: 'park_map', 5:'house_of_mirrors'}
    #print the dictionary so the user knows what to look for 
    print(map_dic)
    
   
    
   #wrap in a while statement because we need a true valid response before we can move to the next function 
    while True:
        #grab user input as a string
    
        destination = int(input('Make your selection: Type 1-5\n Press enter when complete'))
        #check that user input matches a valid function in the function library
        if destination <= 5:
            #pass the user input to the function dictionary, call the function based on which key was selected 
            destination = str(destination)
            function_dictionary[destination]()
            break
        else:
            #if input is invalid, stay in the loop and repeat the input function
            print('invalid selection:\n Please pick from the list above.')
            










#create a master dictionary of all functions in the program. 
function_dictionary = {'6':time_ran_out, '7':into ,'8': park_entrance ,'1': guillotine_ride, '2': petting_zoo, '3' :shooting_gallery, '4': park_map, '5':house_of_mirrors }








#order in which the game progresses
#into function where the park is introduced
into()
#where we decide if we want to enter and meet the attendant
park_entrance()
#first ride, can we avoid death
guillotine_ride()
#the main menu, where users can select which rides to go on. 
park_map()
