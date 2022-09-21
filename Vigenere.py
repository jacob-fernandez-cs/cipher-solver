
class Vigenere:
    def __init__(self, cipher, key):
        self.cipher = cipher.upper()
        self.key = key.upper()
        self.plainTextList = []
        self.spacePosList = []

    def decrypt(self):
        self.checkSpaces()
        self.cipher = self.cipher.replace(" ", "")
        keyLength = len(self.key)
        keyPos = 0
        for c in self.cipher:
            keyShift = ord(self.key[keyPos]) - ord('A')
            plainTextShift = (ord(c) - ord('A') - keyShift + 26) % 26
            plainTextChar = chr(ord('A') + plainTextShift)
            self.plainTextList.append(plainTextChar)
            keyPos = (keyPos + 1) % keyLength


    def getPlainText(self):
        currentPos = 0
        nextSpacePos = 0
        finalPlainText = ''

        for p in self.plainTextList:
            if len(self.spacePosList) != 0 and self.spacePosList[nextSpacePos] == currentPos:
                finalPlainText += ' ' + p
                currentPos += 2
                if nextSpacePos < len(self.spacePosList) - 1:
                    nextSpacePos += 1
            else: 
                finalPlainText += p
                currentPos += 1
            
        return finalPlainText


    def checkSpaces(self):
        pos = 0
        for c in self.cipher:
            if c == ' ':
                self.spacePosList.append(pos)
            pos = pos + 1

    def test(self):
        self.cipher = 'gimco lc wzgdrfie bmqyeq mt noqojeg'
        self.key = 'zebra'
        self.decrypt()
        print('STARTING TEST\n')
        print(self.getPlainText(), end='\n')

#solve = Vigenere('', '')
#solve.test()