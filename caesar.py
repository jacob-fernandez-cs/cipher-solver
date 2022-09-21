import sys
from textwrap import wrap
from spellchecker import SpellChecker

class Caesar:
    cipher = ""
    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.found = False

        
    def get_letter(self, new_key, letter):
        if letter in self.alphabet:
            return self.alphabet[new_key]
        return letter
    def encryption(self):
        message = input("Enter message: ").upper()
        encrypted_text = ""
        for letter in message:
            new_key = (self.alphabet.find(letter) + self.key) % len(self.alphabet)
            encrypted_text = encrypted_text + self.get_letter(new_key, letter)
        print("Encrypted Message: {}".format(encrypted_text))
    
    def caesarSolve(self, decrypt):
         spell = SpellChecker()
         caesarDecrypt = decrypt.split()
         #print(caesarDecrypt)
         misspelled = spell.unknown(caesarDecrypt)
         if (len(misspelled) < 1):
            print("the cipher above is correct! ")
            #print(decrpyt)
            #self.found = True
            return caesarDecrypt
            print("* ")

    def getfound(self):
        return self.found
    
    def decryption(self, cipher):
            message = cipher.upper()
            decrypted_text = ""
            list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            splitAtNum = len(message)
            thislist = []
            for i in list:
                for letter in message:
                    new_key = (self.alphabet.find(letter) - (ord(i) - 65)) % len(self.alphabet) # off sets the current letter with the new key
                    decrypted_text = decrypted_text + self.get_letter(new_key, letter) # decrypt using the new character found using the new key
            # **************************COMMENT OUT WHICHEVER PRINT STATEMENT BELOW IN THE FOR LOOP ****************************************
            for i in range(0, len(decrypted_text), splitAtNum):
                result = self.caesarSolve(decrypted_text[i:i+splitAtNum])
                if result != None:
                    self.found = True
                    break
                #thislist.append(decrypted_text[i:i+splitAtNum])
            #print(thislist)
               
            return result



"""
    def keyword_picker(self):
        print("Keyword must contain exactly one letter A - Z")
        keyword = input("Enter keyword: ").upper()
        if keyword not in self.alphabet:
            print('Invalid Key word entered')
            sys.exit()
        return ord(keyword) - 65
"""
#test = Caesar()
##test.encryption()
#test.decryption("Etstqd ldrrzfdr vgdm ozrrdc sgqntfg sgd rxrsdl zqd dmbqxosdc zmc uhbd udqrz")


