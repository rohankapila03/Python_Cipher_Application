# encryption.py
# Rohan Kapila, ENDG 233 F21
# A terminal-based encryption application capable of both encoding and decoding text when given a specific cipher.
# You may optionally import the string module from the standard Python library. No other modules may be imported.
# Remember to include docstrings for your functions and comments throughout your code.

### Define your functions here
def cipher_dict(cipher):
    """
    Creates dictionary for cipher and lowecase alphabet by combining lowercase list and cipher list
    
    Arguments:
    cipher -- cipher_key_checked, list representing no duplicates and lowercase cipher.

    Returns:
    Returns a dictionary of lowercase alphabet as key value and cipher with no uppercase or duplicates. 

    """
    import string
    alphabet = string.ascii_lowercase
    alphabet_list = list(alphabet)
    pair_alphabet_list_and_cipher = zip(alphabet_list,cipher)
    dict_pair_alphabet_listres = dict(pair_alphabet_list_and_cipher)
    return dict_pair_alphabet_listres

def encoded_text(text,cipher):
    """
    Uses user text and dictionary created to encode the users text.

    Arguments:
    text -- user_text is string that user inputs as their text to be encoded or decoded
    cipher -- cipher_key, this is the dictionary created by the user between their cipher with no duplicates and lowercase and lowercase alphabet.

    Returns:
    Returns an encoded text by adding values to blank string for letters in the user text as cipher dictionary values.

    """
    encode_text = ""
    for letters in text:
        encode_text += cipher[letters]
    return encode_text

def decoded_text(text, cipher):
    """
    Uses user text and the dictionary created to decode the text
    
    Arguments:
    text -- user_text is a string inputted by the user that will aloow the string to be decoded or encoded
    cipher -- cipher_key is the dictionary created user that correlates the alphabet and a cipher
    
    Return:
    return decoded string by adding values to blank string by finding cipher value is equal to letter of text than add the value used for cipher.

    """
    
    decode_text = ""
    for letter in text:
        for value in cipher:
            if cipher[value] == letter:
                decode_text += value
    return decode_text

print("ENDG 233 Encryption Program")

### Add your main program code here
user_choice = None                                                                                  #allows the code to enter the while loop
while user_choice != 0:
    user_choice = int(input('Select 1 to encode or 2 to decode your message, select 0 to quit: '))  #ask user wether they would like to encode decode or exit the program
    if user_choice == 0:                                                                            #if user input is 0 the break function exits the loop and prints concluding statement
        break
    user_text = input('Please enter the text to be processed: ')                                    #asks user to input there text
    list_user_text = list(user_text)                                                                #changes user_text to list
    user_cipher = input('Please enter the cipher text: ')                                            #user input cipher
    user_cipher_lowercase = user_cipher.lower()                                                     #changes user cipher into only lowercase letters
    cipher_list = list(user_cipher_lowercase)                                                       #makes lowercase cipher into a list
    cipher_list_checked = []         
    [cipher_list_checked.append(x) for x in cipher_list if x not in cipher_list_checked]            #adds cipher list into new list while ensuring previous values added are not the same as current value being added using list comprehension
    if len(cipher_list_checked) == 26 and user_cipher.isalnum():                                    #checks if lenght of cipher after no duplicates is 26 and all entries are letter or numbers if these are true allows user to continue by encoding or decoding
        print('your cypher is valid')
        cipher_key = cipher_dict(cipher_list_checked)                                               #creates variable as cipher dictionary by referring to cipher_dict function only if cipher is valid
        if user_choice == 1:                                                                        #nested if statement for user choice
            text_encoded = encoded_text(user_text, cipher_key)                                      #calling encoded_text function and saving the value as text encoded                    
            print('your output is:',text_encoded)                                                   #print saved value stored in encoded_text which is stored in variable text_encoded
        if user_choice == 2:                                                                        #nested if statement if cipher valid and user inputs 2 the decode function will be called
            text_decoded = decoded_text(user_text, cipher_key)                                      #call decode_text function and store return as variable 
            print('your output is:',text_decoded)                                                   #print stored value of decoded function that is called

    else:
        print('your cipher must contain 26 uniue elements of a-z or 0-9')                           #if cipher is invalid tell user to input new one by re running while loop

print('Thank you for using the encryption program.')                                                #if user input option 0 print concluding statement by exiting loop.