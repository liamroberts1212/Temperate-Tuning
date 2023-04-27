
import pygame
import sys
import button
import random
import os
import re
import math
import requests
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
    pygame.mixer.find_channel().play( pygame.mixer.Sound( "rain1.mp3"))#format( min(3, math.ceil(int(weather['precipitation'][0:-1])/10/2))) ) )

    #same thing for wind
    if (int(wind[0]) > 1):
        z = 1
        #pygame.mixer.find_channel().play( pygame.mixer.Sound( "wind.wav") ) 
    print(temp, hum, wind)
    

    #same thing for humidity + temp

def get_location_data():

    city = input("Enter City: ")
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

if __name__ == "__main__":
    WINDOW_WIDTH    = 400
    WINDOW_HEIGHT   = 400
    WINDOW_SURFACE  = pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE

    DARK_BLUE = (   3,   5,  54)

    # This is my path
    path = "C:\\Users\\Liam\\Documents\\CSCI\\DL\\notes"

    # to store files in a list
    filelist = []
 
    # dirs=directories
    for (root, dirs, file) in os.walk(path):
        for f in file:
            filelist.append('notes\\' + f)

    sample_sets = dict();
    c_major = ["notes\\C3.mp3","notes\\D3.mp3",
                    "notes\\E3.mp3","notes\\F3.mp3",
                    "notes\\G3.mp3","notes\\A3.mp3",
                    "notes\\B3.mp3","notes\\C4.mp3", "notes\\D4.mp3",
                    "notes\\E4.mp3"]
    guitar = ["cookedsamples\\1_h.mp3", "cookedsamples\\2_h.mp3", "cookedsamples\\3_h.mp3",
              "cookedsamples\\4_h.mp3", "cookedsamples\\5_h.mp3","cookedsamples\\6_h.mp3",
              "cookedsamples\\1E.mp3", "cookedsamples\\1A.mp3", "cookedsamples\\1D.mp3", "cookedsamples\\1G.mp3", "cookedsamples\\1B.mp3",
              "cookedsamples\\1ee.mp3", "cookedsamples\\2E.mp3", "cookedsamples\\2A.mp3", "cookedsamples\\2D.mp3", "cookedsamples\\2G.mp3",
              "cookedsamples\\2B.mp3", "cookedsamples\\2ee.mp3"]
    alt_tuning = [
        "cookedsamples\\full_harm_1.mp3", "cookedsamples\\full_harm_2.mp3", "cookedsamples\\full_harm_3.mp3",
        "cookedsamples\\open_strum.mp3", "cookedsamples\\low3.mp3", "cookedsamples\\riff1.mp3", "cookedsamples\\riff1_high.mp3",
        "cookedsamples\\riff2.mp3", "cookedsamples\\riff2_high.mp3", "cookedsamples\\top4.mp3",
         
                 "cookedsamples\\low_trill.mp3", "cookedsamples\\high_trill.mp3",

        "cookedsamples\\big1.mp3",
        "cookedsamples\\big1_high.mp3",
        "cookedsamples\\big2.mp3", 

        "cookedsamples\\elow_harm.mp3", "cookedsamples\\Alow_h.mp3", "cookedsamples\\dlow_h.mp3",
        "cookedsamples\\glow_h.mp3","cookedsamples\\blow_h.mp3","cookedsamples\\elow_high.mp3",
        "cookedsamples\\lowe.mp3","cookedsamples\\a.mp3","cookedsamples\\d.mp3"
        ,"cookedsamples\\g.mp3","cookedsamples\\b.mp3","cookedsamples\\ehigh.mp3"
    ]
    alt_tuning_detuned = ["cookedsamples\\full_harm_1.mp3", "cookedsamples\\full_harm_2.mp3", "cookedsamples\\full_harm_3.mp3",
        "cookedsamples\\open_strum.mp3", "cookedsamples\\low3.mp3", "cookedsamples\\riff1.mp3", "cookedsamples\\riff1_high.mp3",
        "cookedsamples\\riff2.mp3", "cookedsamples\\riff2_high.mp3", "cookedsamples\\top4.mp3",
         
                 "cookedsamples\\low_trill.mp3", "cookedsamples\\high_trill.mp3",

        "cookedsamples\\big1.mp3",
        "cookedsamples\\big1_high.mp3",
        "cookedsamples\\big2.mp3", 

        "cookedsamples\\elow_harm.mp3", "cookedsamples\\Alow_h.mp3", "cookedsamples\\dlow_h.mp3",
        "cookedsamples\\glow_h.mp3","cookedsamples\\blow_h.mp3","cookedsamples\\elow_high.mp3",
        "cookedsamples\\altlowe.mp3","cookedsamples\\alta.mp3","cookedsamples\\altd.mp3"
        ,"cookedsamples\\altg.mp3","cookedsamples\\altb.mp3","cookedsamples\\altehigh.mp3"]
    
    
    

    

    piano = [
        "notes\\C3.mp3",
        "notes\\Db3.mp3",
        "notes\\D3.mp3",
        "notes\\Eb3.mp3",
        "notes\\E3.mp3",
        "notes\\F3.mp3",
        "notes\\Gb3.mp3",
        "notes\\G3.mp3",
        "notes\\Ab3.mp3",
        "notes\\A3.mp3",
        "notes\\Bb3.mp3",
        "notes\\B3.mp3",

        "notes\\C4.mp3",
        "notes\\Db4.mp3",
        "notes\\D4.mp3",
        "notes\\Eb4.mp3",
        "notes\\E4.mp3",
        "notes\\F4.mp3",
        "notes\\Gb4.mp3",
        "notes\\G4.mp3",
        "notes\\Ab4.mp3",
        "notes\\A4.mp3",
        "notes\\Bb4.mp3",
        "notes\\B4.mp3",

        "notes\\C5.mp3",
        "notes\\Db5.mp3",
        "notes\\D5.mp3",
        "notes\\Eb5.mp3",
        "notes\\E5.mp3",
        "notes\\F5.mp3",
        "notes\\Gb5.mp3",
        "notes\\G5.mp3",
        "notes\\Ab5.mp3",
        "notes\\A5.mp3",
        "notes\\Bb5.mp3",
        "notes\\B5.mp3",
    ]
    
    tunings = [alt_tuning, alt_tuning_detuned]


    
    print(len(active_notes))

    ### initialisation
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.set_volume(10)
    window = pygame.display.set_mode( ( WINDOW_WIDTH, WINDOW_HEIGHT ), WINDOW_SURFACE )
    pygame.display.set_caption("Soundscape Generator")

    ### sound
    # create separate Channel objects for simultaneous playback
    pygame.mixer.set_num_channels(300)

    # Rain sound from: https://www.freesoundslibrary.com/sound-of-rain-falling-mp3/ (CC BY 4.0)
    rain_sound = pygame.mixer.Sound( 'sound-of-rain-falling-mp3.mp3' )
    #pygame.mixer.find_channel().play( rain_sound, -1 )   # loop the rain sound forever



    clock = pygame.time.Clock()
    done = False
    weather = get_location_data()
    create_soundscape(weather)

    notes = 0
    #if it is raining, initalize ctr to one (detune samples)
    if (int(weather['humidity'][0:-1])) > 50:
        active_notes = tunings[1]
        print("setting default tuning to de-tuned\n")
    else:
        active_notes = tunings[0]

    while not done:
        # Handle user-input
        for event in pygame.event.get():
            if ( event.type == pygame.QUIT ):
                done = True
            elif ( event.type == pygame.KEYDOWN ):
                if ( event.key == pygame.K_q ):                      
                    pygame.mixer.find_channel().play( pygame.mixer.Sound( active_notes[0] ) )
                if ( event.key == pygame.K_w ):                   
                    pygame.mixer.find_channel().play( pygame.mixer.Sound( active_notes[1] ) )
                if ( event.key == pygame.K_e):
                    pygame.mixer.find_channel().play( pygame.mixer.Sound( active_notes[2] ) )
                if ( event.key == pygame.K_r):
                    pygame.mixer.find_channel().play( pygame.mixer.Sound( active_notes[3] ) )
                if ( event.key == pygame.K_t):
                    pygame.mixer.find_channel().play( pygame.mixer.Sound( active_notes[4] ) )
                if ( event.key == pygame.K_y):
                    pygame.mixer.find_channel().play( pygame.mixer.Sound( active_notes[5] ) )
                if ( event.key == pygame.K_u):
                    pygame.mixer.find_channel().play( pygame.mixer.Sound( active_notes[6] ) )
                if ( event.key == pygame.K_i):
                    pygame.mixer.find_channel().play( pygame.mixer.Sound( active_notes[7] ) )
                if ( event.key == pygame.K_o):
                    pygame.mixer.find_channel().play( pygame.mixer.Sound( active_notes[8] ) )
                if ( event.key == pygame.K_p):
                    pygame.mixer.find_channel().play( pygame.mixer.Sound( active_notes[9] ) )
                if ( event.key == pygame.K_a ):                      
                    pygame.mixer.find_channel().play( pygame.mixer.Sound( active_notes[10] ) )
                if ( event.key == pygame.K_s ):                   
                    pygame.mixer.find_channel().play( pygame.mixer.Sound( active_notes[11] ) )
                if ( event.key == pygame.K_d):
                    pygame.mixer.find_channel().play( pygame.mixer.Sound( active_notes[12] ) )
                if ( event.key == pygame.K_f):
                    pygame.mixer.find_channel().play( pygame.mixer.Sound( active_notes[13] ) )
                if ( event.key == pygame.K_g):
                    pygame.mixer.find_channel().play( pygame.mixer.Sound( active_notes[14] ) )
                if ( event.key == pygame.K_h):
                    pygame.mixer.find_channel().play( pygame.mixer.Sound( active_notes[15] ) )
                if ( event.key == pygame.K_j):
                    pygame.mixer.find_channel().play( pygame.mixer.Sound( active_notes[16] ) )
                if ( event.key == pygame.K_k):
                    pygame.mixer.find_channel().play( pygame.mixer.Sound( active_notes[17] ) )
                if ( event.key == pygame.K_l):
                    pygame.mixer.find_channel().play( pygame.mixer.Sound( active_notes[18] ) )
                if ( event.key == pygame.K_z):
                    pygame.mixer.find_channel().play( pygame.mixer.Sound( active_notes[19] ) )
                if ( event.key == pygame.K_x ):                      
                    pygame.mixer.find_channel().play( pygame.mixer.Sound( active_notes[20] ) )
                if ( event.key == pygame.K_c ):                   
                    pygame.mixer.find_channel().play( pygame.mixer.Sound( active_notes[21] ) )
                if ( event.key == pygame.K_v):
                    pygame.mixer.find_channel().play( pygame.mixer.Sound( active_notes[22] ) )
                if ( event.key == pygame.K_b):
                    pygame.mixer.find_channel().play( pygame.mixer.Sound( active_notes[23] ) )
                if ( event.key == pygame.K_n):
                    pygame.mixer.find_channel().play( pygame.mixer.Sound( active_notes[24] ) )
                if ( event.key == pygame.K_m):
                    pygame.mixer.find_channel().play( pygame.mixer.Sound( active_notes[25] ) )
                if ( event.key == pygame.K_COMMA):
                    pygame.mixer.find_channel().play( pygame.mixer.Sound( active_notes[26] ) )
                if ( event.key == pygame.K_BACKSLASH):
                    notes = not notes
                    active_notes = tunings[notes]
                        
                    
                    

        # Window just stays blue
        window.fill( DARK_BLUE )
        #customButton1.process(window)
        pygame.display.flip()

        # Clamp FPS
        clock.tick_busy_loop(60)

    pygame.quit()