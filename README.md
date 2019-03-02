# Apex-Legends-Anti-Recoil
Simple python script to randomize anti recoil in any video game. @thecamwars HF


Hey guys, I recently wrote a small python script for my brother for the game Apex Legends. All the script does is when you toggle it on by numlock, and then hold down your left click, it will bring your reticle down a couple of pixels. I added a randomization feature where it will choose from intervals of time, horizontal travel, and verticle.

This is all really basic. My brother has used it for 2 weeks and no ban yet, so I decided to give it to you guys. This should work in any randomized recoil pattern game great, even though apex isnt, I believe anti-cheat will ban if we exactly match the spray pattern.
I would love to see what you guys can come up with if you edit the source code.

This is python, and if you do not know how to use it, don't. I am not going to make an exe out of it.
I also hear that Powershell has less chance of being detected, so run it in PowerShell.
Requirements are python3
optional VB
And you will need to PIP these
import pyautogui
import time
import win32api
import random
import keyboard


The default button to toggle is "num lock" but you can change it if you look up keyboard call signs.
I have brought the settings to the very top so you can change them easily.
You will have to go to the range to fine tune in your weapon, but the basic one I have right now I used for all the guns regardless.
For havoc, google spin up time and put that as min_fireate = blah blah.


Again, Let me know if you like it, hopefully it'll go undetected for a while, but always good to use in other games.
