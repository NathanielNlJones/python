#-------------------------------------------------------------------------------
# LA9.py
# Name: Nathaniel Jones
# Python Version: 2.XX or 3.XX
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: 
#-------------------------------------------------------------------------------
# Notes to grader: 
#-------------------------------------------------------------------------------
# Code: Code starts here
#-------------------------------------------------------------------------------

def encryptor(message, offset):
    '''
    Encrypts message by offset
    Returns the encrypted message
    '''
    encryptedMessage = "" #Initialize string to accumulate encrypted values
    #iterates over input string, for each letter:
    for letter in message:
        ASCII = ord(letter) #convert to ASCI
        encryptedASCII = ASCII + offset #apply offset
        encryptedLetter = chr(encryptedASCII) #convert back to character
        encryptedMessage += encryptedLetter #concatate onto initialized string
    return encryptedMessage #return encrypted string
    
def decryptor(encryptedMessage, offset):
    '''
    Decrypts encrypted_message by offset
    Returns the decrypted message
    '''
    decryptedMessage = "" #Initialize string to accumulate decrypted values
    #iterates over input string, for each letter:
    for letter in encryptedMessage:
        ASCI = ord(letter) #convert to ASCI
        decryptedASCI = ASCI - offset #reverse offset
        decryptedLetter = chr(decryptedASCI) #convert back to character
        decryptedMessage += decryptedLetter #reassemble decrypted string
    return decryptedMessage #return decrypted string

def main():
    
    print ('\nStart of IT 109 Caesar cypher program\n')

    choice = 'Y'
    while choice != 'N':
        #user menu to ask for message and offset
        message = input("Enter a short message to be encrypted (50 characters or less):")
        offset = int(input("Enter an integer offset value to be used as a key (1-10:)"))
        #call encryptor function
        encryptedMessage = encryptor(message, offset)
        #call decryptor function
        decryptedMessage = decryptor(encryptedMessage, offset)
        #print encrypted and decrypted message
        print("Encrypted message: {}".format(encryptedMessage))
        print("Decrypted message: {}".format(decryptedMessage))
        choice = input('\nDo you want to encrypt and decrypt another message? (Y/N): ')  
            
    print ('\nEnd of Caesar cypher program')

main()
            
            
