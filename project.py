
import pygame
import random
import os
import re
from bs4 import BeautifulSoup
from requests_html import HTMLSession

session = HTMLSession()
# Window size

active_notes = []

def create_scale():
    '''funciton to create a scale based off of some input
       returns a list of notes to be used in the scale, automatically
       mapped to keys.'''
    active_notes.clear()
    temp_notes = []
    for i in range(10):
        temp_notes.append(random.randint(0,88))
    temp_notes = sorted(temp_notes)
    for i in range(len(temp_notes)):
        active_notes.append(temp_notes[i])
    print(active_notes)
       
def create_soundscape(weather):

    print(weather)

    is_raining = re.findall(".*rain.*", weather['weather_now'].lower())
    temp = re.findall(".*\d+.*", weather['temp_now'])
    hum = re.findall(".*\d+", weather['humidity'])
    wind = re.findall(".*\d+", weather['wind'])
    #compute volume of rain sound based off if it is raining versus if it is
    #not raining
    #if (len(is_raining) > 0):
        #it is raining, determine the audio clip to play
        #print( math.ceil(int(weather['precipitation'][0:-1])/10/2) )
    #pygame.mixer.find_channel().play( pygame.mixer.Sound( "rain1.mp3"))#format( min(3, math.ceil(int(weather['precipitation'][0:-1])/10/2))) ) )

    #same thing for wind
    #if (int(wind[0]) > 1):
    #    z = 1
        #pygame.mixer.find_channel().play( pygame.mixer.Sound( "wind.wav") ) 
    #print(temp, hum, wind)
    

    #same thing for humidity + temp

def get_location_data():

    #city = input("Enter City: ")
    city = 'troy'
    url = "https://www.google.com/search?q=weather+{}".format(city)
    response = session.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    result = {}
    result['region'] = soup.find("div", attrs={"id": "wob_loc"}).text
    result['temp_now'] = soup.find("span", attrs={"id": "wob_tm"}).text
    result['dayhour'] = soup.find("div", attrs={"id": "wob_dts"}).text
    result['weather_now'] = soup.find("span", attrs={"id": "wob_dc"}).text
    result['precipitation'] = soup.find("span", attrs={"id": "wob_pp"}).text
    result['humidity'] = soup.find("span", attrs={"id": "wob_hm"}).text
    result['wind'] = soup.find("span", attrs={"id": "wob_ws"}).text

    return result

def setup_samples():

    WINDOW_WIDTH    = 400
    WINDOW_HEIGHT   = 400
    WINDOW_SURFACE  = pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE

    # This is my path
    path = "C:\\Users\\Liam\\Documents\\CSCI\\TT\\Temperate-Tuning\\sets"
    
    sets = dict()
    # dirs=directories
    for (root, dirs, file) in os.walk(path): 
        set = []
        for f in file:
            set.append(f)
        sets[root] = set

    for key in sets:
        print(key, end="\n\n\n\n")

    ### init
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.set_volume(10)
    window = pygame.display.set_mode( ( WINDOW_WIDTH, WINDOW_HEIGHT ), WINDOW_SURFACE )
    pygame.display.set_caption("Soundscape Generator")

    ### sound
    # create separate Channel objects for simultaneous playback
    pygame.mixer.set_num_channels(300)

    keys = list(map(ord, list("qwertyuiopasdfghjklzxcvbnm,.")))
    keymaps = [x for x in range(27)]
    soundboard = dict(zip(keys, keymaps))
    

    weather = get_location_data()
    create_soundscape(weather)
    #pygame.mixer.find_channel().play( pygame.mixer.Sound( active_notes[0] ) )
    npath = "C:\\Users\\Liam\\Documents\\CSCI\\TT\\Temperate-Tuning\\sets\\guitar"

    return [sets, soundboard, npath, window]

def run(sets, soundboard, npath, window):
    done = False
    clock = pygame.time.Clock()
    while not done:
        # Handle user-input
        for event in pygame.event.get():
            if ( event.type == pygame.QUIT ):
                done = True
            elif ( event.type == pygame.KEYDOWN ):
                if (event.key not in soundboard):
                    print('Key Pressed: not mapped')
                    continue

                print("Key Pressed:", soundboard[event.key])
                pygame.mixer.find_channel().play( pygame.mixer.Sound( npath + '\\' + sets[npath][soundboard[event.key]] ) )

    pygame.display.flip()

    # Clamp FPS
    clock.tick_busy_loop(60)

    pygame.quit()

    return

if __name__ == "__main__":
    vals = setup_samples()
    run(vals[0], vals[1], vals[2], vals[3])

