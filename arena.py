#!/usr/bin/python3

class Kostka:
    """
    Simuluje Hrací kostku
    """

    def __init__(self, steny = 6):
        """
        Inicializuje počet stěn, neveřejný argument.
        """
        self.__pocet_sten = steny

    def __str__(self):
        """
        Vrátí textovou reprezentaci.
        """
        return "Kostka má {} stěn".format(self.__pocet_sten)

    def vratPocetSten(self):
        """
        Vrátí počet stěn
        """
        return self.__pocet_sten

    def hod(self):
        """
        Hodí kostkou
        """
        import random as _random
        return _random.randint(1, self.__pocet_sten)

class Bojovnik:
    def __init__(self, jmeno, zivoty, utok, obrana, kostka):
        """
        jmeno = jméno bojovníka
        zivoty = aktuální životy
        max_zivoty = maxmimální životy, na začátku se předpokládá plné zdraví
        utok = útok 
        obrana = obrana
        kostka = ukazatel na společnou instanci kostky
        """
        self.__jmeno = jmeno
        self.__zivoty = int(zivoty)
        self.__max_zivoty = int(zivoty)
        self.__utok = int(utok)
        self.__obrana = int(obrana)
        self.__kostka = kostka

    def __str__(self):
        return self.__jmeno

    @property
    def nazivu(self):
        """
        Vrací True, když žije, False když umře.
        Je to atribut (@property)
        """
        return self.__zivoty > 0

    def zivotg(self):
        """
        Vrací vizulizovaný počet životů.
        př. [####    ]
        """
        celkem = 21
        pocet = int(self.__zivoty / self.__max_zivoty * celkem)
        if pocet <= 0:
            pocet = 1
        return "[{}{}]".format("#"*pocet, " "*(celkem - pocet))    
