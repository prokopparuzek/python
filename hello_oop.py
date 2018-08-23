#!/usr/bin/python3

class Hello:
    """
    Třída co tě pozdraví.
    """
    
    def __init__(self, text):
        self.text=text
    def pozdrav(self):
        """
        Provede pozdrav dle textu zadaného při inicializaci.
        """
        print("{}".format(self.text))

    def pozdrav_jmenem(self, jmeno):
        """
        Pozdravi jmenem. 
        """
        print("{} {}".format(self.text, jmeno))
    def vraceny_pozdrav(self, jmeno):
        """
        Vrati pozdrav.
        """
        return "{} {}".format(self.text, jmeno)

text = input("Zadejte text: ")
zdrav = Hello(text)
zdrav.pozdrav()
jmeno = input("Zadej jmeno: ")
zdrav.pozdrav_jmenem(jmeno)
print(zdrav.vraceny_pozdrav(jmeno))
