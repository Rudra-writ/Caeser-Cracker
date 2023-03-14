from spellchecker import SpellChecker
import re

class CaeserCracker:

    def __init__(self,text, shift):
        self.text = text
        self.shift = shift

    #Method to cipher the input message using the message and the input key
    def caesar_cipher(self):
        encrypted = ""
        #Looping through each character in the input message.
        #If the the character is an english alphabet, 
        # converting the character to ASCII value using 'ord()', substracting 97 (ASCII for 'a') if character is lower case or 65 (ASCII for 'A')
        #  if character is upper case to get the index of alphabet, 
        # adding the cypher key (shift). The result is then operated by 'mod 26' because there are only 26 english alphabets.  
        # Finally the resultant ASCII equivalent is converted back to an english alphabet using 'chr()'
        for char in self.text:
            if char.islower():    
                encrypted = (encrypted + chr((ord(char) + self.shift - 97) % 26 + 97)) if char.isalpha() else (encrypted + char)
            else:
                encrypted = (encrypted + chr((ord(char) + self.shift - 65) % 26 + 65)) if char.isalpha() else (encrypted + char)
    
        return encrypted    #Returning the encrypted message
    

    #Method to decipher the user input
    def caesar_decipher(self):

        spell = SpellChecker() #Creating a spellchecker object
        decrypted_messages = []
        text = re.sub('[^a-zA-Z0-9 \n\.\,\!\?]', ' ', self.text)    #Cleaning the input message to retain only words, numbers and english punctuations and convert the rest to spaces
        
        for key in range(1,27):    #Iterating from 1 to 26 to create a list of 26 decrypted messages by shifting the characters in the encrypted message by 1 through 26. (Trying all possible combinations)
            decrypted = ""
            for char in text:
                if char.islower():
                    decrypted = (decrypted + chr((ord(char) - key - 97) % 26 + 97)) if char.isalpha() else (decrypted + char)
                else:
                    decrypted = (decrypted + chr((ord(char) - key - 65) % 26 + 65)) if char.isalpha() else (decrypted + char)
            decrypted_messages.append(decrypted)     
        
        #From the list of decrypted messages creating another list which contains the number of correct english words in each of the decrypted message, using the correction() method of the SpellChecker object created above
        decrypted_messages_count = list(map(lambda message: sum(1 for word in message.split() if word == spell.correction(word)), decrypted_messages))
        #Selecting the decrypted message which has the maximum number of correct english words as the final cracked message to display
        decrypted_message = decrypted_messages[decrypted_messages_count.index(max(decrypted_messages_count))]
        
        return decrypted_message    #Returning the decrypted message



