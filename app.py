
#import dependencies
import time
from PIL import Image    
from playsound import playsound  
import     sys        
from threading import Timer      
import os                                                      
import random
import pandas as pd
import functions_file
from random_word import RandomWords



#order in which the game progresses
#into function where the park is introduced
functions_file.intro()
#where we decide if we want to enter and meet the attendant
functions_file.park_entrance()
#user goes to the park map and can pick which ride to get on.
functions_file.park_map()

