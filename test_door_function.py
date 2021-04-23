import keyboard



def door_push():
    count = 0
    #keyboard.wait('A')


    while count < 50:
        print('keep mashing b')

        if keyboard.is_pressed('b') == True:
            count += 1
            if count == 50:
                break
            else:
                pass
        #else:
            #print('you diddnt press anything')



door_push()

















