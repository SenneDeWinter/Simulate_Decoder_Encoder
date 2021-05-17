#!/usr/bin/env python
"""
Uitdaging één:

Gebruik de encoder/decoder: https://github.com/KDGThomasDeWitte/decoder_simulate2 (Koppelingen naar een externe site.)
Je maakt een keuzemenu (tekstgebaseerd) in console waarbij je kiest voor een tekst in te lezen die encodeert of decodeert.
Je kan dan via de console een tekst inlezen en deze kan je dan encoderen/decoderen.
Je test je code uitvoerig en zorgt ervoor dat er geen foutmeldingen zijn!

Uitdaging twee:

Ofwel: Je leest een tekstbestand in in de plaats van tekst in te voeren via console.
Ofwel: Je maakt een GUI waarbij je de tekst kan inlezen
Ofwel beide ;).
Je test je code uitvoerig en zorgt ervoor dat er geen foutmeldingen zijn!
"""


from decoder import *                                                      #To import the decoder library
import os                                                                  #To import the os library
import sys                                                                 #To import the sys library


__author__ = "Senne De Winter"
__email__ = "senne.dewinter@student.kdg.be"
__status__ = "Production"


def main():
    print("Wat wil je doen?")                                              #To ask what the user wants to do
    print("1: Encode")                                                     #To show the first option
    print("2: Decode")                                                     #To show the second option

    keuze = input()                                                        #To give the user a choice

    if keuze == "1":                                                       #To execute when the users choice was encode
        print("Geef een tekst in:")                                        #To ask the user to insert text
        text = input()                                                     #To input the text
        print(get_code(text))                                              #To print the encoded text
        restart = input("Wil je herstarten? [j/n]\n")                      #To ask if the users wants to restart
        if restart == "j":                                                 #To execute if the answer was yes
            os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) #To restart the script
            print("\n")                                                    #To print a blank line
        elif restart == "n":                                               #To execute if the answer was no
            print("Het programma wordt afgesloten")                        #To confirm that the script will shut down
            sys.exit(0)                                                    #To shut down the script
        else:
            os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) # To restart the script if the answer wasn't yes or no

    elif keuze == "2":                                                     #To execte when the users choice was decode
        print("Geef een tekst in:")                                        #To ask the user to insers text
        text = input()                                                     #To input the text
        print(get_decode(text))                                            #To print the decoded text
        restart = input("Wil je herstarten? [j/n]\n")                      #To ask if the user wants to restart
        if restart == "j":                                                 #To execute when the answer was yes
            os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) #To restart the script
        elif restart == "n":                                               #To execute if the answer was no
            print("Het programma wordt afgesloten")                        #To confirm that the script will shut down
            sys.exit(0)                                                    #To shut down the script
        else:
            os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) # To restart the script if the answer wasn't yes or no

    else:
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)     #To restart the script if the answer wasn't 1 or 2


if __name__ == '__main__':  # code to execute if called from command-line
    main()
