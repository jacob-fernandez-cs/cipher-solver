
import math
from spellchecker import SpellChecker


class transpo:

   

    def __init__(self):
       self.message = "whats up"
       self.found = False

    def autosolve(self, myMessage):
        #myMessage= 'Cenoonommstmme oo snnio s s c'
        
       
        spell = SpellChecker()


        for x in range(1,150):
          plaintext = self.decrypt(x, myMessage.upper())
          plaintext = str(plaintext)
         
          decrpyt = plaintext.split() #make the returned decrypted string a list of strings the string must be separated by spaces 
         
          misspelled = spell.unknown(decrpyt) # creates a list of all misspelled words , if the length of the list is < 1 than it is the correct text print it

          if (len(misspelled) < 1):
            print("* ")
            
            self.found = True
            return decrpyt
            print("* ")

     

          

    def getfound(self):
        return self.found


    def decrypt(self,key, message):
       colummns = math.ceil(len(message) / key)
       rows = key
       emptyBoxes = (colummns * rows) - len(message)
       crackedText = [''] * colummns
  
       col = 0
       row = 0
   
       for i in message:
          crackedText[col] += i
          col += 1
          if (col == colummns) or (col == colummns - 1 and row >= rows - emptyBoxes):
             col = 0 
             row += 1 
         
         
       #print(plaintext)
       #return ''.join(plaintext)
       return "".join(crackedText)
 
  
  
#test = transpo()

#print(test.autosolve("Cenoonommstmme oo snnio s s c"))
