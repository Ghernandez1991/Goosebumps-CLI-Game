
from dataclasses import dataclass
import sys
import time
from audio import AudioManager
from pathlib import Path
from PIL import Image
from threading import Timer
from player import Player

    

@dataclass
class Horrorland():
    player: Player
    park_dictionary =  {
                "7": "time_ran_out",
                "8": 'intro',
                "9": 'park_entrance',
                "10": 'breakout_room',
                "6": 'leave_park',
                "1": 'guillotine_ride',
                "2": 'petting_zoo',
                "3": 'shooting_gallery',
                "4": 'park_map',
                "5": 'house_of_mirrors',
            }
  
    # into function when the game starts
    def intro(self) -> None:
        #create path to song
        song_path = Path(r"audio\Goosebumps_theme.mp3")

        audio_1 =AudioManager(song_path)
        audio_1.play_audio()
        # play intro music
        #playsound(r"audio\Goosebumps_theme.mp3", False)
        # time the terminal to the music
        time.sleep(1)
        print(
            """
    ╭╮╭╮╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╭╮╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╭╮
    ┃┃┃┃┃┃╱╱┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╭╯╰╮╱╱╱┃┃╱┃┃╱╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱╱╱┃┃
    ┃┃┃┃┃┣━━┫┃╭━━┳━━┳╮╭┳━━╮╰╮╭╋━━╮┃╰━╯┣━━┳━┳━┳━━┳━┫┃╱╱╭━━┳━╮╭━╯┃
    ┃╰╯╰╯┃┃━┫┃┃╭━┫╭╮┃╰╯┃┃━┫╱┃┃┃╭╮┃┃╭━╮┃╭╮┃╭┫╭┫╭╮┃╭┫┃╱╭┫╭╮┃╭╮┫╭╮┃
    ╰╮╭╮╭┫┃━┫╰┫╰━┫╰╯┃┃┃┃┃━┫╱┃╰┫╰╯┃┃┃╱┃┃╰╯┃┃┃┃┃╰╯┃┃┃╰━╯┃╭╮┃┃┃┃╰╯┃
    ╱╰╯╰╯╰━━┻━┻━━┻━━┻┻┻┻━━╯╱╰━┻━━╯╰╯╱╰┻━━┻╯╰╯╰━━┻╯╰━━━┻╯╰┻╯╰┻━━╯"""
        )
        # flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
        # time the terminal to the music
        time.sleep(2)
        print(
            """´´´´´´´´´´´´´ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´`
    ´´´´´´´´´´´´´´´´´¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´
    ´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´
    ´´´´´´´´´´´´´¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´
    ´´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´
    ´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´`´´´´´´´´´´´¶¶´´´´´´´´´´`
    ´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´
    ´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´
    ´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´
    ´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´
    ´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´
    ´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´
    ´´´´´´´´´´´¶¶´¶¶´´´¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´¶¶´¶¶´´´´´´´´´´´
    ´´´´´´´´´´´´¶¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶¶¶´´´´´´´´´´´
    ´´´´´´´´´´´´´¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶´´´´´´´´´´´´´
    ´´´´¶¶¶´´´´´´´¶¶´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´¶¶´´´´´´¶¶¶¶´´´
    ´´´¶¶¶¶¶´´´´´¶¶´´´¶¶¶¶¶¶¶´´´¶¶¶´´´¶¶¶¶¶¶¶´´´¶¶´´´´´¶¶¶¶¶¶´´
    ´´¶¶´´´¶¶´´´´¶¶´´´´´¶¶¶´´´´¶¶¶¶¶´´´´¶¶¶´´´´´¶¶´´´´¶¶´´´¶¶´´
    ´¶¶¶´´´´¶¶¶¶´´¶¶´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´¶¶¶¶´´´´¶¶¶´
    ¶¶´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´¶¶
    ¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶¶´´´´´´¶¶¶¶¶¶¶¶
    ´´¶¶¶¶´¶¶¶¶¶´´´´´´¶¶¶¶¶´´´´´´´´´´´´´´¶¶¶´¶¶´´´´´¶¶¶¶¶¶´¶¶¶´
    ´´´´´´´´´´¶¶¶¶¶¶´´¶¶¶´´¶¶´´´´´´´´´´´¶¶´´¶¶¶´´¶¶¶¶¶¶´´´´´´´´
    ´´´´´´´´´´´´´´¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶´´´´´´´´´´´´´´
    ´´´´´´´´´´´´´´´´´´¶¶´¶¶´¶´¶´¶´¶´¶´¶´¶´¶´¶¶´´´´´´´´´´´´´´´´´
    ´´´´´´´´´´´´´´´´¶¶¶¶´´¶´¶´¶´¶´¶´¶´¶´¶´´´¶¶¶¶¶´´´´´´´´´´´´´´
    ´´´´´´´´´´´´¶¶¶¶¶´¶¶´´´¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶´¶¶¶¶¶´´´´´´´´´´´´
    ´´´´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶´´´´´´´´´´´´´´´´´¶¶´´´´´´¶¶¶¶¶¶¶¶¶´´´´
    ´´´¶¶´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´´
    ´´´´¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶´´´´
    ´´´´´´¶¶´´´¶¶¶´´´´´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´´´´¶¶¶´´´¶¶´´´´´´
    ´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´
    ´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´
    """
        )
        # flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
        # time the terminal to the music
        time.sleep(2)
        print("Have a scary day!!!!")
        # flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
        # print(u"\u2620".encode('utf-8'))
        print()
        # flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
        # time the terminal to the music
        time.sleep(3)


        # entrance function , does the user want to play
    def park_entrance(self) -> None:
        print("You enter the abandonded carnival and are met by a ticket stand.")
        # flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
        # time the terminal to the music
        time.sleep(3)
        print(" You slowly and cautiously approach the booth.")
        # flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
        # time the terminal to the music
        time.sleep(3)
        print("No one is in the booth")
        # flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
        # time the terminal to the music
        time.sleep(3)
        print("You stick your head in and shout hello! ")
        # flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
        # time the terminal to the music
        time.sleep(3)
        # show image of the ticket attendant
        img = Image.open(r"images\attendant.PNG")
        img.show()
        # play the attendant welcome message
        song_path = Path(r"audio\Welcome_to_horrorland.mp3")
        audio_1 =AudioManager(song_path)
        audio_1.play_audio()

        #playsound(r"audio\Welcome_to_horrorland.mp3")
        print('Admission is free. You"re our guest today.')
        # flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
        # time the terminal to the music
        time.sleep(3)
        print(
            "Do you wish to enter the park?\nPress 1 to continue.\nPress 2 to exit the park."
        )
        # flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
        # user selects whether they want to enter the park or not
        entrance_selection = int(input("Enter your selection now:"))
        if entrance_selection == 1:
            song_path_2 = Path(r"audio\Enjoy_horrorland.mp3")
            audio_2 =AudioManager(song_path_2)
            audio_2.play_audio()
            # if they enter, play the enjoy message
            #playsound(r"audio\Enjoy_horrorland.mp3")
        elif entrance_selection == 2:
            # if the dont enter, kill them
            print(
                "You have nothing to fear, but fear itself.\n You have terminated the game\nSo we have terminated you\nGoodbye"
            )
            # flush after every print because otherwise the terminal does not update real time
            sys.stdout.flush()
            sys.exit("User bitched out")
        # catch any other selections
        else:
            print("The park paton has made a fatal error\n")
            # flush after every print because otherwise the terminal does not update real time
            sys.stdout.flush()


    def park_map(self) -> None:
        song_path = Path(r"audio\Goosebumps (Theme Song).mp3")
        audio =AudioManager(song_path)
        audio.play_audio()

        #playsound(r"audio\Goosebumps (Theme Song).mp3", block=False)
        print("Unclear of where to go next, you lookaround for a map.")
        sys.stdout.flush()
        # time the terminal
        time.sleep(3)
        print(
            'You see the map near by. It reads "HorrorLand: The Most Tragic Place on Earth"'
        )
        time.sleep(3)
        # create dictionary of current functions
        map_dic = {
            1: "guillotine_ride",
            2: "petting_zoo",
            3: "shooting_gallery",
            4: "park_map",
            5: "house_of_mirrors",
            6: "leave_park",
        }
        # print the dictionary so the user knows what to look for
        print(map_dic)
        # wrap in a while statement because we need a true valid response before we can move to the next function
        while True:
            # grab user input as a string

            destination = int(
                input("Make your selection: Type 1-6\n Press enter when complete")
            )
            # check that user input matches a valid function in the function library
            if destination <= 6:
                # pass the user input to the function dictionary, call the function based on which key was selected
                destination = str(destination)
                ride = self.park_dictionary[destination]
                try:
                    method_to_call = getattr(self, ride)
                    method_to_call()
                except:
                    print(f"No ride named '{ride}' found.")

                break
            else:
                # if input is invalid, stay in the loop and repeat the input function
                print("invalid selection:\n Please pick from the list above.")




    


    def guillotine_ride(self) -> None:
        print("After gathering your tickets, you see a large sign.")
        # flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
        # time the terminal to the music
        time.sleep(2)
        print("The ride of your life, ")
        # flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
        # time the terminal to the music
        time.sleep(1)
        print('You"ll never forget')
        # flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
        # time the terminal to the music
        time.sleep(1)
        print("Welcome to Death Mountain")
        # flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
        # time the terminal to the music
        time.sleep(1)
        print("Guranteed to be a slicing good time")
        # flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
        # time the terminal to the music
        time.sleep(2)
        # where does the user want to sit on the ride. This affects how much reaction time they get
        seat_selection = int(
            input("Where do you want to sit?: 1 for front, 2 for middle, 3 for rear.")
        )
        # create a dictionary with the three user inputs
        seat_dic = {1: "front", 2: "middle", 3: "rear"}
        # grab the value , based on the user key selection
        seat_choice = seat_dic[seat_selection]
        # F print where the user decided to get on the roller coaster
        print(f"You get into your seat at the {seat_choice} of the ride.")
        # flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
        # play climbing roller coaster music

        song_path = Path(r"audio\Climbing_the_coaster.mp3")
        audio =AudioManager(song_path)
        audio.play_audio()
        #playsound(r"audio\Climbing_the_coaster.mp3", False)
        # time the terminal to the music
        time.sleep(2)
        print("The cart starts to move.")
        # flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
        # time the terminal to the music
        time.sleep(2)
        print('You"re pushed to the back of your seat')
        # flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
        # time the terminal to the music
        time.sleep(2)
        print("You await what is at the top of the hill.")
        # flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
        # time the terminal to the music
        time.sleep(5)
        print("You get higher and higher off the ground")
        # flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
        # time the terminal to the music
        time.sleep(5)
        print("You squeeze the handle")
        # flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
        # time the terminal to the music
        time.sleep(10)
        print("Your heart begins to race")
        # flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
        # time the terminal to the music
        time.sleep(5)
        print("You finally reach the top")
        # flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()

        # show image at the top of the roller coaster
        img = Image.open(r"images\top_of_the_coaster.PNG")
        img.show()
        # play audio for the ride down
        song_path_2 = Path(r"audio\Descent_from_top.mp3")
        audio_2 =AudioManager(song_path_2)
        audio_2.play_audio()

        #playsound(r"audio\Descent_from_top.mp3")
        # based on user seat selection, their reaction time will be shorter at the front of the ride, longer at the rear.
        if seat_selection == 1:
            time_to_react = 3
        elif seat_selection == 2:
            time_to_react = 4
        elif seat_selection == 3:
            time_to_react = 5
        else:
            # catch all other entries
            print(
                "You did not secure yourself to the ride.\n Have fun falling to your death. \n Goodbye"
            )
            sys.exit("User fell out of the ride")
        # call timer fuction, arguements are the users time_to_react(based on seat selection) and the time_ran_out function
        # the timer runs for anywhere from 3-5 seconds, and then calls the time_ran_out function of the user doesnt press a button
        t = Timer(time_to_react, self.player.take_damage, args=(100,))
        # start timer
        t.start()
        # prompt the user for input and quick
        user_input = input("Quick!\n Press any key.\n Better duck quick!\n Press Enter")
        # if the user managed to press a button
        if user_input != None:
            print("You managed to save your head by ducking")
            # flush after every print because otherwise the terminal does not update real time
            sys.stdout.flush()
            # cancel the timer function and get out
            t.cancel()
        # if the user failed to input anything
        elif user_input == None:
            # call time_ran_out_function which kills the player and the game
            Player.take_damage(100)
        else:
            print(
                "You managed to crack your skull on a passing branch.\n Have fun falling unconcious and not waking up.\n Goodbye"
            )
            # flush after every print because otherwise the terminal does not update real time
            sys.stdout.flush()
            sys.exit("User hit their head")
        self.park_map()
    
    
