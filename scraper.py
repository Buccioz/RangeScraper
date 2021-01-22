import requests
import termcolor
import colorama
import time
import os

from os import system, name 
from termcolor import *
from colorama import *

Token = '363eb54d8747d2'

def banner():

    cprint("""         
                         _____                           _____                                
                        |  __ \                         / ____|                               
                        | |__) |__ _ _ __   __ _  ___  | (___   ___ _ __ __ _ _ __   ___ _ __ 
                        |  _  // _` | '_ \ / _` |/ _ \  \___ \ / __| '__/ _` | '_ \ / _ \ '__|
                        | | \ \ (_| | | | | (_| |  __/  ____) | (__| | | (_| | |_) |  __/ |   
                        |_|  \_\__,_|_| |_|\__, |\___| |_____/ \___|_|  \__,_| .__/ \___|_|   
                                            __/ |                            | |              
                                            |___/                            |_|            

""", 'magenta');
    cprint("""
                        :::::::::::::::::::IP RANGE SCRAPER FOR IPINFO.IO:::::::::::::::::::::
                        :::::::::::::::::::::::::Woozy & Davidb003::::::::::::::::::::::::::::                    
                                                                                                """, 'white');
                                                                                

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 



def main():

    clear()
    banner()
    while(True):
        domain = input(Fore.MAGENTA + "Domain: " + Fore.WHITE)
        f = open(domain + '.lst', "a")
        response = requests.get('http://ipinfo.io/ranges/' + domain + '?token=' + Token)
        print(response.text, file=f)
        f.close()


main()