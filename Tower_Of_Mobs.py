#! /usr/bin/python3

################################################
# Author : Spyro24                             #
# Script Name :Tower of mobs                   #
# File name : Tower_Of_Mobs.py                 #
# IDE : Thonny                                 #
# Python version : 3.10.6                      #
# License : GPLv2                              #
# Description : A simple fight tower game.     #
################################################

from random import randint

start = False
hp = 0 #player's HP
xp = 0 #player's xp point's
lv = 0 #player's level
max_hp = 100 #Player's max hp
round_ = 0 #python has a command 'round'
mob = [" Slime ", "Zombie", "Skeleton ", ""] #a list of all mobs and states of the mobs
mob_xp = [3, 5, 10]
mob_kp = [20, 35, 50]
mob_ap = [2, 5, 10]
mob_drop =["Potion", "AP Boost", "HP Boost"]
drop_per = [10, 1, 5] #drop "wahrscheinlichkeit" of a item
inv_items = [] #a simple inventar
item_amount = [] #amount of items, if items equals zero than python delete the item
ro_fin = False #Round finish
chose  = 0 #
mkp = 0
mbc = 0

def rp(score, plr, HP, LV, mob, mob_hp): # Round print. A Simple Ui to interface with the programm.
        
    if score >= 10000:
        print("you win the game.\nYou have reached the end of the tower.")
        exit()
        
    sc = str(score)
    tmp = 4 - len(sc)
    for n in range(0, tmp):
        sc = "0" + sc
        
    hp = str(HP)
    tmp = 4 - len(hp)
    for n in range(0, tmp):
        hp = " " + hp
        
    lv = str(LV)
    tmp = 4 - len(lv)
    for n in range(0, tmp):
        lv = " " + lv
        
    mob = str(mob)
    tmp = 14 - len(mob)
    for n in range(0, int(tmp/2)):
        mob = mob + " "
        mob = " " + mob
    mobmobmobmob = mob
    
    # Print the simple ui with the infos
    print(f'+------------------------------------------+')                           
    print(f'|Round: {sc}                 Player : {plr}|')
    print(f'|Level: {lv}                     HP : {hp} |')
    print(f'|                                          |')
    print(f'|              {mobmobmobmob}              |')

def finscr(plr, HP, sc, XP):
        
    sc = str(score)
    tmp = 4 - len(sc)
    for n in range(0, tmp):
        sc = "0" + sc
        
    hp = str(HP)
    tmp = 4 - len(hp)
    for n in range(0, tmp):
        hp = " " + hp
        
    xp = str(XP)
    tmp =4 - len(xp)
    for n in range(0, tmp):
        xp = " " + xp
    
    # Print the simple ui with the infos
    print(f'+------------------------------------------+')                           
    print(f'|Round: {sc}                 Player : {plr}|')
    print(f'|Level: {lv}                     HP : {hp} |')
    print(f'|                                          |')
    print(f'|               Round Finish               |')
    print(f'|                                          |')
    print(f'| {plr} get {xp}                           |')
    
try:
    while 1:
        if start == False:
            name = input("Chose your name : ")
            if len(name) > 5 :
                print("Err : Name too long\nErr : Max 5 Characters\n")
            
            if len(name) == 0 :
                print("Err : No Name input\nErr : Please input a name\n")
            
            if 0 < len(name) < 5 :
                full = 5 - len(name)
                for n in range(0, full):
                    name = name  + " "
                start = True
            
            if len(name) == 5 :
                start = True
        
        if start == True :
            rp(round_ , name, "SW", "", " Slime", "")
            exit()
            if ro_fin == True :
                round_ =+ 1
                ro_fin = False
except KeyboardInterrupt:
    exit()