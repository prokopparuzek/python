#!/usr/bin/python3

import sys
import random
from unidecode import unidecode

class Hangman:
    def __init__(self, wfile):
        """
        Inicializuje hangmana,
        přečte soubor zadaný jako argument,
        očekává na každém řádku 1 slovo.
        Poté náhodně vybere slovo a 
        inicializuje hádací řetězec.
        Inicializuje správně hádaná písmena.
        """
        words = []
        with open(wfile, mode="r", encoding="utf-8") as dic:
            for string in dic:
                string = string.rstrip()
                words.append(string.lower())
        self.__word = words[random.randint(0,len(words) - 1)]
        self.__word = unidecode(self.__word)
        self.__puzzle = "-"*len(self.__word)
        self.guess = "ěščřžýáíéúů"

    def isIn(self, guess):
        """
        Zkontroluje zda je zadaný řetězec v hádaném slově.
        """
        self.guess += guess
        return str(guess) in self.__word

    def updatePuzzle(self, guess):
        """
        Doplní hádané slovo, dle zadaného písmene.
        """
        self.guess += guess
        self.__puzzle = ""
        for c in self.__word:
            if c in self.guess:
                self.__puzzle += c
            else:
                self.__puzzle += "-"
        return self.__puzzle

    @property
    def getPuzzle(self):
        return self.__puzzle

    @property
    def getWord(self):
        return self.__word

if __name__ == "__main__":
    try:
        hangman = Hangman(sys.argv[1])
    except IndexError:
        print("Zadejte soubor slov, jako argument")
        sys.exit(2)
    count = input("Kolik chcete pokusů? ")
    try:
        count = int(count)
    except ValueError:
        print("Číslo prosím!")
        sys.exit(1)
    print("Hádané slovo má {} písmen.".format(len(hangman.getPuzzle)))
    print("Vše je malým písmem a bez interpunkce")
    print("{}".format(hangman.getPuzzle));
    for i in range(count):
        print("Pokus číslo {}.".format(i + 1))
        c = input("Zadejte odhadované písmeno. ")
        c = str(c)
        while 1 < len(c) or c in hangman.guess:
            c = input("Pouze jeden znak prosím! ||\nUž jste toto písmeno použil||\nObsahuje diakritiku: ")
        hangman.updatePuzzle(c)
        if hangman.isIn(c):
            print("Správně, ještě {} pokusů".format(count - i - 1))
            hangman.updatePuzzle(c)
        else:
            print("Špatně, ještě {} pokusů".format(count - i - 1))
        print("{}".format(hangman.getPuzzle));
        if "-" not in hangman.getPuzzle:
            print("Vyhral jsi!")
            sys.exit(0)
    print("Prohrál jsi.\nHádané slovo bylo: {}".format(hangman.getWord))
