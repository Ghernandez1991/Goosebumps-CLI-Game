#import dependencies
import time
from PIL import Image    
from playsound import playsound  
import     sys        
from threading import Timer      
import os                                                      
import random
import pandas as pd
from random_word import RandomWords
import numpy as np


#helper function for using timer
def time_ran_out():
    print("You couldnt avoid the axe")
    time.sleep(5)
    #flush after every print because otherwise the terminal does not update real time
    sys.stdout.flush()
    #open image signifiying the player died
    img = Image.open(r'images\headless.PNG')
    img.show()
    #exit the terminal because the game is over
    os._exit(0)
    
#into function when the game starts
def intro():
    #play intro music
    playsound(r'audio\Goosebumps_theme.mp3', False)
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
    img = Image.open(r'images\attendant.PNG')
    img.show()
    #play the attendant welcome message
    playsound(r'audio\Welcome_to_horrorland.mp3')
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
        playsound(r'audio\Enjoy_horrorland.mp3')
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
    print('Welcome to Death Mountain')
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
    playsound(r'audio\Climbing_the_coaster.mp3', False)
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
    img = Image.open(r'images\top_of_the_coaster.PNG')
    img.show()
    #play audio for the ride down
    playsound(r'audio\Descent_from_top.mp3')
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
    park_map()


#create functions for remaining parts of the story
def petting_zoo():
    print('petting zoo')


#create functions for remaining parts of the story
def shooting_gallery():
    print('shooting gallery')


def leave_park():
    sys.exit('Thanks for visiting Horrorland. It was to die for')

#create a main menu where the user can choose which ride(function) they want to play
def park_map():
    playsound(r'audio\Goosebumps (Theme Song).mp3', False)
    print('Unclear of where to go next, you lookaround for a map.')
    sys.stdout.flush()
    #time the terminal 
    time.sleep(3)
    print('You see the map near by. It reads "HorrorLand: The Most Tragic Place on Earth"')
    time.sleep(3)
    #create dictionary of current functions 
    map_dic = {1: 'guillotine_ride', 2: 'petting_zoo', 3 :'shooting_gallery', 4: 'park_map', 5:'house_of_mirrors', 6:'leave_park'}
    #print the dictionary so the user knows what to look for 
    print(map_dic)
    #wrap in a while statement because we need a true valid response before we can move to the next function 
    while True:
        #grab user input as a string
    
        destination = int(input('Make your selection: Type 1-6\n Press enter when complete'))
        #check that user input matches a valid function in the function library
        if destination <= 6:
            #pass the user input to the function dictionary, call the function based on which key was selected 
            destination = str(destination)
            function_dictionary[destination]()
            break
        else:
            #if input is invalid, stay in the loop and repeat the input function
            print('invalid selection:\n Please pick from the list above.')
            













def house_of_mirrors():
    
    playsound(r'audio\House_of_mirrors.mp3')
    print("You enter the house of mirrors")
    sys.stdout.flush()
    time.sleep(3)
    print("You are presented with a choice")
    sys.stdout.flush()
    time.sleep(3)
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
    img = Image.open(r'images\in_the_hall_of_mirrors.PNG')
    img.show()
    time.sleep(5)
    print('You find yourself in a hall of mirrors.')
    sys.stdout.flush()
    time.sleep(3)
    print("You proceed into the unknown.")
    sys.stdout.flush()
    time.sleep(3)

    if direction_choice in left_choices:
        #scenario 1
        print('The door slams shut')
        sys.stdout.flush()
        time.sleep(5)
        print('The room is dark')
        sys.stdout.flush()
        time.sleep(5)
        playsound(r'audio\Where_are_you.mp3')
        print('You find yourself trapped in\n The room is dark. \n No one can hear your screams')
        sys.stdout.flush()
        time.sleep(5)
        img = Image.open(r'images\demon.PNG')
        img.show()
        print("You must make your selections carefully, or else you will trapped forever.")
     

        #to do
        #call create game board function--creates game board and generates a starting position and startign exit
        #must get starting position , end position
        
        #call move_functions to get the index values for rows and columns 
        #once you have index values, you can then process the users forward , left right or back. 



        #grab user input. forward left or right or backwards
        #call forward left or right/back function based on what they say
        #probably an if statment- 
        

     
        sys.stdout.flush()
    elif direction_choice in right_choices:
        #scenario 2
        print('scenario 2')
    else:
        print('You managed to get trapped and lost for eternity.\n Have fun screaming for days, and then starving to death.\n Goodbye')
        #flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
        sys.exit('User got lost and died.')


    park_map()





def house_of_mirrors_gameboard():
    #set the number of strikes(mistakes) the user is allowed to 0. So we can count them
    #strikes = 0
    #user gets a random number of chances between 3 and 5
    #chances = random.randrange(3,5)
    #list of rows-indexing starts at 0
    rows = [0,1,2,3]
    #list of columns 
    columns = ['a', 'b', 'c', 'd']
    #create a dataframe which will function as our scoreboard
    global df
    df = pd.DataFrame(index = rows,columns = columns)
    while True:

        #we want to users starting y position to be between 0 and 3
        starting_y_axis = random.randrange(0,4)
        #we want the starting y position to be a value in list [columns ]
        starting_x_axis = random.choice(columns)
        #concatonate together, convert into to str
        global starting_position
        starting_position = starting_x_axis + str(starting_y_axis)
        #create random exit position
        #we want to users starting y position to be between 0 and 3
        exit_y_axis = random.randrange(0,4)
        #we want the starting y position to be a value in list [columns ]
        exit_x_axis = random.choice(columns)
        #concatonate together, convert into to str
        global exit_position
        exit_position = exit_x_axis + str(exit_y_axis)


        #todo
        #create death traps as well
        #want these to be random. 
        punjee_pit_starting_position_yaxis = random.randrange(0,4)
        punjee_pit_starting_position_xaxis = random.choice(columns)
        
        global punjee_pit_starting_position
        punjee_pit_starting_position = punjee_pit_starting_position_xaxis + str(punjee_pit_starting_position_yaxis)
        
        if starting_position==exit_position:
            pass
        elif starting_position == punjee_pit_starting_position:
            pass
        elif exit_position==punjee_pit_starting_position:
            pass
        else:
            break

    #print how lucky the user is.
    #print(f"You get {chances} chances to make it out alive")
    print('in the darkness, youre not sure where to do.')
    print(f"Your starting position is {starting_position}")
    print(f"your exit position is {exit_position}")
    print(f"your punjee pit position is {punjee_pit_starting_position}")

    #grab the first value of the starting_position(column). The value is originally a string, so we have to conver the second value to int
    converted_start_x_point = starting_position[0]
    #grab the second value of the starting_position(row). The value is originally a string, so we have to conver the second value to int
    converted_start_y_point = int(starting_position[1])
    #use index function to find which index poisition the starting row/column is in the lists of rows and columns
    indexed_start_x_point = columns.index(converted_start_x_point)
    #use index function to find which index poisition the starting row/column is in the lists of rows and columns
    indexed_start_y_point = rows.index(converted_start_y_point)
    print(f"The start row index is {indexed_start_y_point}, the start column index is{indexed_start_x_point}")
    #using the row and column index values, place 'starting_point' onto our game board(csv file)
    df.iat[indexed_start_y_point, indexed_start_x_point] = 'starting_point'


    #grab the first value of the exit_position(column). The value is originally a string, so we have to convert the second value to int
    converted_exit_x_point = exit_position[0]
    #grab the second value of the exit_position(row). The value is originally a string, so we have to convert the second value to int
    converted_exit_y_point = int(exit_position[1])
    #use index function to find which index poisition the starting row/column is in the lists of rows and columns
    indexed_exit_x_point = columns.index(converted_exit_x_point)
    #use index function to find which index poisition the starting row/column is in the lists of rows and columns
    indexed_exit_y_point = rows.index(converted_exit_y_point)
    print(f"The exit row index is {indexed_exit_y_point}, the exit column index is{indexed_exit_x_point}")
    #using the row and column index values, place 'exit_point' onto our game board(csv file)
    df.iat[indexed_exit_y_point, indexed_exit_x_point] = 'exit_point'

    #put punjee pit to dataframe
    #grab the first value of the punjee_pit(column). The value is originally a string, so we have to convert the second value to int
    converted_punjee_x_point = punjee_pit_starting_position[0]
    #grab the second value of the punjee_pit(row). The value is originally a string, so we have to convert the second value to int
    converted_punjee_y_point = int(punjee_pit_starting_position[1])
    #use index function to find which index poisition the starting row/column is in the lists of rows and columns
    indexed__punjee_start_x_point = columns.index(converted_punjee_x_point)
    #use index function to find which index poisition the starting row/column is in the lists of rows and columns
    indexed_punjee_start_y_point = rows.index(converted_punjee_y_point)
    print(f"The start row index for punjee is {indexed_punjee_start_y_point}, the start column index for punjee is{indexed__punjee_start_x_point}")
    #using the row and column index values, place 'exit_point' onto our game board(csv file)
    df.iat[indexed_punjee_start_y_point, indexed__punjee_start_x_point] = 'punjee_pit'
    #print DF so we can see all the items on the board
    print(df)
    #write the df to a csv for use later
    df.to_csv('current_game_board.csv')

#call function for testing
house_of_mirrors_gameboard()


#function to pass starting position to- it finds its position (row and column) in the list which makes up the checkerboard
def move_function(starting_position):
    #get list of rows in the house of mirrors 
    rows = [0,1,2,3]
    #get list of column names from house of mirrors 
    columns = ['a', 'b', 'c', 'd']
    #grab the row name from starting_position passed to the function(convert to int since list has ints)
    row = int(starting_position[1])
    #grab the column name as the first leter from starting_position passed to the function 
    column = starting_position[0]
    #check to make sure they are right
    print(column,row)
    #if our row value is in the list
    if row in rows:
        #get the index position of our row value from the list
        value_of_row = rows.index(row)
        print(f' The row value {row} is in the {value_of_row} postion in the list rows')
        
    else:
        print('item not in list')
    
    if column in columns:
        #get the index position of our column value from the list
        value_of_column = columns.index(column)
        print(f' The row value {column} is in the {value_of_column} postion in the list columns')
    else:
        print('item not in list')
        

    return value_of_column, value_of_row
#uncomment to test
move_function('d3')

#put in index values from the move_function as arguement
def forward_function(value_of_column,value_of_row):
    #wrap all of this in a try except block because if we hit a 'wall' you are going to get an index error
    try:
        #check all the rows and columns in the dataframe and look for the string 'current_position' . If found, it returns an array
        current_position_count = np.column_stack([df[col].str.contains("current_position", na=False) for col in df])
        #if the value is found in the array, the value is greater than 1
        if current_position_count.any()>0:
            #if so, we want to find the previous 'current_position' and overwrite it with a nan
            df[df.eq('current_position')] = np.nan
        
            
            #get list of rows in the house of mirrors 
            rows = [0,1,2,3]
            #get list of column names from house of mirrors 
            columns = ['a', 'b', 'c', 'd']
            #calculate new forward row position by grabing existing value from the list(row) - 1.  - 1 because we are moving up(forward) in the matrix
            new_forward_row_position = rows[value_of_row - 1]
            #calculate new forward column position by taking the index value from value of column 
            new_forward_column_position = columns[value_of_column]
            print(new_forward_column_position,new_forward_row_position)
            
            #print current position in gameboard
            #convert column from string(abcd) to the index value in list
            new_forward_column_position = columns.index(new_forward_column_position)
            #take the index value and place 'current position' in the spreadsheet
            df.iat[new_forward_row_position,new_forward_column_position] = 'current_position'
            print(f"the new forward row position is {new_forward_row_position}, the new_forward_column_position is {new_forward_column_position}  ")
            print(df)       
    except IndexError:
        print('catching the index error')
        print('user hit the wall, cant turn right. Make a new selection')
    return new_forward_column_position, new_forward_row_position


#put in index values from the move_function
forward_function(2,0)


#put in index values from the move_function
def backward_function(value_of_column,value_of_row):
    #wrap all of this in a try except block because if we hit a 'wall' you are going to get an index error
    try:
        #check all the rows and columns in the dataframe and look for the string 'current_position' . If found, it returns an array
        current_position_count = np.column_stack([df[col].str.contains("current_position", na=False) for col in df])
        #if the value is found in the array, the value is greater than 1
        if current_position_count.any()>0:
            #if so, we want to find the previous 'current_position' and overwrite it with a nan
            df[df.eq('current_position')] = np.nan
        #get list of rows in the house of mirrors 
        rows = [0,1,2,3]
        #get list of column names from house of mirrors 
        columns = ['a', 'b', 'c', 'd']
        #calculate new forward row position by grabing existing value from the list(row) - 1.  - 1 because we are moving up(forward) in the matrix
        new_backward_row_position = rows[value_of_row + 1]
        #calculate new forward column position by taking the index value from value of column 
        new_backward_column_position = columns[value_of_column]
        
        print(new_backward_column_position,new_backward_row_position)
        
        #print current position in gameboard
        #convert column from string(abcd) to the index value in list
        new_backward_column_position = columns.index(new_backward_column_position)
        #take the index value and place 'current position' in the spreadsheet
        df.iat[new_backward_row_position,new_backward_column_position] = 'current_position'
        print(f"the new backward row position is {new_backward_row_position}, the new_backward_column_position is {new_backward_column_position}  ")
        print(df)      
    except IndexError:
        print('catching the index error')
        print('user hit the wall, cant turn right. Make a new selection')
    return new_backward_column_position, new_backward_row_position


#put in index values from the move_function
backward_function(0,3)

def left_function(value_of_column,value_of_row):
    #wrap all of this in a try except block because if we hit a 'wall' you are going to get an index error
    try:
        #check all the rows and columns in the dataframe and look for the string 'current_position' . If found, it returns an array
        current_position_count = np.column_stack([df[col].str.contains("current_position", na=False) for col in df])
        #if the value is found in the array, the value is greater than 1
        if current_position_count.any()>0:
            #if so, we want to find the previous 'current_position' and overwrite it with a nan            
            df[df.eq('current_position')] = np.nan
        #get list of rows in the house of mirrors 
        rows = [0,1,2,3]
        #get list of column names from house of mirrors 
        columns = ['a', 'b', 'c', 'd']
        #calculate new forward row position by grabing existing value from the list(row) - 1.  - 1 because we are moving up(forward) in the matrix
        new_left_column_position = columns[value_of_column - 1]
        #calculate new forward column position by taking the index value from value of column 
        new_left_row_position = rows[value_of_row]
        
        print(new_left_column_position,new_left_row_position)
        
        #print current position in gameboard
        #convert column from string(abcd) to the index value in list
        new_left_column_position = columns.index(new_left_column_position)
        #take the index value and place 'current position' in the spreadsheet
        df.iat[new_left_row_position,new_left_column_position] = 'current_position'
        print(f"the new left row position is {new_left_row_position}, the new_left_column_position is {new_left_column_position}  ")
        print(df)  
        
    except IndexError:
        print('catching the index error')
        print('user hit the wall, cant turn right. Make a new selection')
    return new_left_column_position, new_left_row_position

left_function(3,3)   


def right_function(value_of_column,value_of_row):
    #wrap all of this in a try except block because if we hit a 'wall' you are going to get an index error
    try:
        #check all the rows and columns in the dataframe and look for the string 'current_position' . If found, it returns an array
        current_position_count = np.column_stack([df[col].str.contains("current_position", na=False) for col in df])
        #if the value is found in the array, the value is greater than 1
        if current_position_count.any()>0:
            #if so, we want to find the previous 'current_position' and overwrite it with a nan  
            df[df.eq('current_position')] = np.nan
        #get list of rows in the house of mirrors 
        rows = [0,1,2,3]
        #get list of column names from house of mirrors 
        columns = ['a', 'b', 'c', 'd']
        #calculate new forward row position by grabing existing value from the list(row) - 1.  - 1 because we are moving up(forward) in the matrix
        new_right_column_position = columns[value_of_column + 1]
        #calculate new forward column position by taking the index value from value of column 
        new_right_row_position = rows[value_of_row]
        
        print(new_right_column_position,new_right_row_position)
        
        #print current position in gameboard
        #convert column from string(abcd) to the index value in list
        new_right_column_position = columns.index(new_right_column_position)
        #take the index value and place 'current position' in the spreadsheet
        df.iat[new_right_row_position,new_right_column_position] = 'current_position'
        print(f"the new right row position is {new_right_row_position}, the new_right_column_position is {new_right_column_position}  ")
        print(df)  
        
        
    except IndexError:
        print('catching the index error')
        print('user hit the wall, cant turn right. Make a new selection')
    return new_right_column_position, new_right_row_position


right_function(2,0)


def punjee_pit():
    print('The room is pitch black')
    print('You cant hear a thing')
    print('You slip and fall')
    playsound(r'audio\Falling.mp3')
    playsound(r'audio\Fatality.mp3')

#punjee_pit()

def breakout_room():
    r= RandomWords()
    
    #user gets a random number of chances between 3 and 5
    strikes = random.randrange(3,5)
    print(strikes)
    screw_ups = 0
    correct_guesses = 0
    
    
    print('The room is pitch')
    print('You cant see a thing')
    player_input = input('Who goes there?')
    print(f'Well {player_input}, you have to correctly respond to my commands, or you will trapped for ever. You have {strikes} strikes until the doors lock forever')
    print('Any typos move the clock closer to 12')
    print('Good luck')
    list_of_words = r.get_random_words(limit=5)
    print(len(list_of_words))
    time_to_react = random.randrange(45,60)
    
    t =Timer(time_to_react,time_ran_out)
    #start timer
    t.start()
    #prompt the user for input and quick    
    
    for item in list_of_words:        
        print(f'Type {item}')
        user_input = input('Quick!\n Type the word above\n Press Enter')
        #if the user managed to press a button
        if user_input==item :
        
            print ('You managed to type the word correctly')
            
            #flush after every print because otherwise the terminal does not update real time
            #sys.stdout.flush()
            #cancel the timer function and get out
            #t.cancel()
            #if the user failed to input anything    
            correct_guesses += 1
        elif user_input != item :
            print('You screwed up')
            #call time_ran_out_function which kills the player and the game
            screw_ups += 1 
            #time_ran_out()
            if screw_ups == strikes:
                time_ran_out()
                
        elif  correct_guesses == len(list_of_words):
            print('You successfully printed all the words')
            player_movement_choice()
        
        else:
            print('You managed to crack your skull on a passing branch.\n Have fun falling unconcious and not waking up.\n Goodbye')
            #flush after every print because otherwise the terminal does not update real time
            sys.stdout.flush()
            sys.exit('User hit their head')

#test function    
breakout_room ()

#create function that accounts for player movement choice. Prompt the user to pick a direction. Everytime they chose, it calls the function to move the respective direction.     
def player_movement_choice():
    player_direction  = int(input('Which direction do you want to go 1:Forward 2:Backrward 3:Left 4:Right'))
    if player_direction == 1:
        forward_function()
    elif player_direction == 2:
        backward_function()
    elif player_direction == 3:
        left_function()
    elif player_direction == 4:
        right_function()
    else:
        print('Invalid selection')
    


function_dictionary = {'7': time_ran_out, '8': intro, '9': park_entrance,
                       '10': breakout_room,
                       '6': leave_park, '1': guillotine_ride,
                       '2': petting_zoo, '3': shooting_gallery,
                       '4': park_map, '5': house_of_mirrors}
#function_dictionary = {'7' : time_ran_out, '8' : intro ,'9' : park_entrance ,'6' : leave_park ,'1': guillotine_ride, '2': petting_zoo, '3' :shooting_gallery, '4': park_map, '5':house_of_mirrors }

 