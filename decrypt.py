# lassoLetter('A', 3) = 'D'
def lassoLetter(letter, shiftAmount):
    letterCode = ord(letter)
    
    begAlphabet = ord('A')
    alphabetSize = 26
        
    decodedLetter = letterCode + shiftAmount
    
    trueLetterCode = begAlphabet + ((letterCode - begAlphabet) + shiftAmount) % alphabetSize  
      
    decodedLetter = chr(trueLetterCode)
    
    return decodedLetter

def lassoWord(word, shiftAmount):
    decodedWord = ''
    
    for letter in word:
        decodedletter = lassoLetter(letter, shiftAmount)
        
        decodedWord += decodedletter
    
    return decodedWord   

print(lassoWord("NCEVY", 13))
print(lassoWord("GPVSUI", 25))
print(lassoWord("UGFLGKG", -18))   
print(lassoWord("WJMMF", -1))

 
    