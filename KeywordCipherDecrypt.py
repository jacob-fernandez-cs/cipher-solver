import sys

from collections import Counter
from textblob import TextBlob
from spellchecker import SpellChecker



class Keyword:
    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.alphabetKeyword = ""
        self.keywordList = []
        self.result = ""
        

    def keyword_picker(self,message):
        #print("Keyword must contain each letter of A-Z exactly once, no letter should repeat itself")
        keyword = message.upper()
        for i in range(len(keyword)):
            pos = i
            for j in range(len(keyword)):
                if pos == j:
                    
                    continue
                elif keyword[i] == keyword[j]:
                    print("Letter {} repeating in keyword".format(keyword[i]))
                    sys.exit()
                
        temp = ""
        for i in range(len(keyword)):
            temp += keyword[i]
        for i in range(26):
            temp += chr(i+65)

        # removing keyword letters from alphabet
        alpha_with_key = ""
        for i in range(len(temp)):
            found = False
            for j in range(len(alpha_with_key)):
                if temp[i] == alpha_with_key[j]:
                    found = True
                    break
                
            if not found:
                alpha_with_key += temp[i]
          

       
        self.alphabetKeyword = alpha_with_key
    

    
    
    
       


    def encryption(self, message):
        message = message.upper()

        encrypted_text = ""
        for i in range(len(message)):
            if message[i] == chr(32):
                encrypted_text += " "
            else:
                counter = 0
                for j in range(len(self.alphabet)):
                    if message[i] == self.alphabet[j]:
                        encrypted_text += self.alphabetKeyword[counter]
                        break
                    else:
                        counter += 1
                

        print("Encrypted Message: {}".format(encrypted_text))


    def decryption(self, message):
        message = message.upper()
        decrypted_text = ""
        for i in range(len(message)):
            if message[i] == chr(32):
                decrypted_text += " "
            else:
                counter = 0
                for j in range(len(self.alphabet)):
                    if message[i] == self.alphabetKeyword[j]:
                        decrypted_text += self.alphabet[counter]
                        break
                    else:
                        counter += 1
               

        #print("Decrypted Text: {}".format(decrypted_text))
        return decrypted_text






    


 

#------------------testing-----------------------

#cipher_user_input = "WHII LT ULSPQH BMMPLXDJBRHIY IBKASBAH PSIHQ DJMLQH BGGDRDLKBI IDJDRBRDLKQ OSR WH GL KLR UBPH JSUC BOLSR RCHJ BQ ILKA BQ LSP TDRKHQQ TSKURDLK WLPFQ BQ HXMHURHG RCH PHBI MPLOIHJ CHPH CLWHVHP DQ RCBR RCH MPLOBODIDRDHQ BPH NSDRH QJBII QL JSIRDMIDUBRDLK LT RCLQH NSDUFIY ALHQ RL HVHK QJBIIHP VBISHQ DKRPLGSUHQ PLSKGDKA HPPLPQ BKG DQ KLR NSDRH SQBOIH"


#emptyList = []

#with open('keywords.txt') as f:
#            emptyList = f.read().splitlines() #make array of keywords 

#test = Keyword() 
#spell = SpellChecker()
           

#for x in emptyList:
#  test.keyword_picker(x)
#  #print(test.decryption(cipher_user_input))
#  print("* ")
#  decrpyt = test.decryption(cipher_user_input).split() #make the returned decrypted string a list of strings the string must be separated by spaces 
#  print(decrpyt)
#  misspelled = spell.unknown(decrpyt) # creates a list of all misspelled words , if the length of the list is < 1 than it is the correct text print it

#  if (len(misspelled) < 1):
#    print("* ")
#    print("the cipher above is correct!")
#    print("* ")




