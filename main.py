import sys
from collections import Counter
from spellchecker import SpellChecker
from KeywordCipherDecrypt import *
from TranspoCipher import *
from Vigenere import *
from caesar import *
from anagram import *


foundKeyword = False
foundVigenere = False
result = []
TranspoCipher = transpo()
caesarCipher = Caesar()
anagramCipher = Anagram()

  

def main():

    running_program = True
    while running_program:
            cipher_user_input = input("\nEnter a cipher to be operated on:\n")

            if cipher_user_input == "QUIT":
                break;
           
            checkT = TranspoCipher.autosolve(cipher_user_input) 
            if TranspoCipher.getfound() == True:
                result = checkT

          

            checkT = caesarCipher.decryption(cipher_user_input)
            if caesarCipher.getfound() == True:
                result = checkT

            checkT = anagramCipher.anagramSolve(cipher_user_input)
            if anagramCipher.getfound() == True:
                result = checkT



            KeywordCipher = Keyword()
            emptyList = []

            with open('keywords.txt') as f:
                        emptyList = f.read().splitlines() #make array of keywords 

            
            spell = SpellChecker() #object created to spell check


            for x in emptyList:
                 KeywordCipher.keyword_picker(x)
                
 
                 decrpyt = KeywordCipher.decryption(cipher_user_input).split() #make the returned decrypted string a list of strings the string must be separated by spaces 
                
                 misspelled = spell.unknown(decrpyt) # creates a list of all misspelled words , if the length of the list is < 1 than it is the correct text print it

                 if (len(misspelled) < 1):
                   print("* ")
                   global foundKeyword 
                   foundKeyword = True
                   result = decrpyt
                   print("* ")

            file = open('VigenereKeys.txt', 'r')
            keysList = file.readlines()
            for vigenere_key in keysList:
                vigenere = Vigenere(cipher_user_input, vigenere_key.replace("\n", ""))
                vigenere.decrypt()
               
                decrypt = vigenere.getPlainText().split() #make the returned decrypted string a list of strings the string must be separated by spaces 
               
                misspelled = spell.unknown(decrypt) # creates a list of all misspelled words , if the length of the list is < 1 than it is the correct text print it
                if (len(misspelled) < 1):
                  
                    result = decrypt
                    global foundVigenere 
                    foundVigenere = True
                    

            print(result)
         
            load_menu()
            



def load_menu():
    
    found_transposition = "Found" if TranspoCipher.getfound() == True else "Not found"
    found_keyword_cipher = "Found" if foundKeyword == True else "Not found"
    found_vigenere_cipher = "Found" if foundVigenere == True else "Not found"
    found_caesar_cipher = "Found" if caesarCipher.getfound() == True else "Not found"
    found_anagram_cipher = "Found" if anagramCipher.getfound() == True else "Not found"

   


    print("\n----Cipher detection---")
    print("Caesar {}".format(found_caesar_cipher))
    print("Keyword Mono-alphabetic {}".format(found_keyword_cipher))
    print("Vigenère {}".format(found_vigenere_cipher))
    print("Anagram {}".format(found_anagram_cipher))
    print("Columnar Transposition {}".format(found_transposition))
  
    


          
                
          

main()
