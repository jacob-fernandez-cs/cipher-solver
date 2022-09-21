from spellchecker import SpellChecker

class Anagram():
    cipher = ""
    def __init__(self):
        self.found = False

    def getfound(self):
        return self.found

    def anagramSolve(self, cipher):
        spell = SpellChecker()
        with open("anagramKeys.txt") as f:
            for line in f:
                    decrpyt = self.solve(cipher, [int(x) for x in line.split(",")]).split()
                    misspelled = spell.unknown(decrpyt)
                    #print(decrpyt)
                    if (len(misspelled) < 1):
                       # print("the cipher above is correct! ")
                        #print(decrpyt)
                        self.found = True
                        return decrpyt
                        print("* ")
                   
    
    #cipher = "oiggn oiggn oiggn oiggn oiggn"
   
    def solve(self, cipher, index):
        cipher_remove_spaces =  cipher.replace(" ", "")
       
        _cipher = list(cipher_remove_spaces)
        str1 = " "
        index 
        
        cipher_split = [_cipher[i:i+len(index)] for i in range(0,len(_cipher),len(index))]
        output = []
        for chunk in cipher_split:
            for elem in range(len(index)):
                try:
                    output.append(chunk[index[elem]])
                except:
                    pass
        
        
        res  = str1.join(output)
        res = res.replace(" ", "")
        test = ""
        counter = 1
        for i in range(len(res)):
            test+=res[i]
            if counter == len(index):
                test+=" "
                counter = 0
            counter += 1
        return test

# try index = [2, 0, 1, 4 ,3]
# 1 2 0 3 to decrypt
# 2 0 1 3 to incrypt

#c = "rnyga earkb noduf lpepa"

#a = Anagram()
##print(a.solve(c))

#a.anagramSolve(c)


