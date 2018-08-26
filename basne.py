#!/usr/bin/python3

import sys
import random

class Poem:
    """
    Generuje náhodné básně.
    """

    def __init__(self, wordsName, rhymesName):
        """
        Argument jsou 2 soubory, 1 se slovy 2 s rymy, mohou byt stejne.
        """
        with open(wordsName, mode="r", encoding="utf-8") as wordsFile:
           self.words = self._readFile(wordsFile)
        if wordsName == rhymesName:
            self.rhymes = self.words
        else:
            with open(rhymesName, mode="r", encoding="utf-8") as rhymesFile:
                self.rhymes = self._readFile(rhymesFile)

    def _readFile(self, File):
        """
        Přečte soubor, vrátí seznam, řádek = člen.
        """
        List = []
        for line in File:
            List.append(line.rstrip())
        return List

    def getLine(self, countW):
        """
        Vrátí 1 řádek z náhodných slov, poslední slovo je vybráno z rýmujcích se slov.
        Vrací větu, 1. slovo velké na konci těčka.
        """
        line = ""
        for _ in range(countW - 1):
            line += self.words[random.randint(0, len(self.words) - 1)].lower()
            line += " "
        line += self.rhymes[random.randint(0, len(self.words) - 1)].lower()
        line += "."
        return line.capitalize()

    def generatePoem(self, countL):
        for _ in range(countL):
            print(self.getLine(random.randint(4,6)))
