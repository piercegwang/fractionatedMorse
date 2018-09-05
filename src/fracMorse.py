import string
import re

morse_keys = {
    'A': '.-',      'B': '-...',    'C': '-.-.',
    'D': '-..',     'E': '.',       'F': '..-.',
    'G': '--.',     'H': '....',    'I': '..',
    'J': '.---',    'K': '-.-',     'L': '.-..',
    'M': '--',      'N': '-.',      'O': '---',
    'P': '.--.',    'Q': '--.-',    'R': '.-.',
    'S': '...',     'T': '-',       'U': '..-',
    'V': '...-',    'W': '.--',     'X': '-..-',
    'Y': '-.--',    'Z': '--..',

    '0': '-----',   '1': '.----',   '2': '..---',
    '3': '...--',   '4': '....-',   '5': '.....',
    '6': '-....',   '7': '--...',   '8': '---..',
    '9': '----.',

    '&': '.-...',   "'": '.----.',  '=': '-...-',
    '@': '.--.-.',  ')': '-.--.-',  '(': '-.--.',
    ':': '---...',  ',': '--..--',  '!': '-.-.--',
    '.': '.-.-.-',  '-': '-....-',  '+': '.-.-.',
    '"': '.-..-.',  '?': '..--..',  '/': '-..-.'
    }

rvmorse_keys = {v: k for k, v in morse_keys.items()}

fractionated_table = [
    '...', '..-', '.. ', '.-.', '.--', '.- ', '. .', '. -', '.  ',
    '-..', '-.-', '-. ', '--.', '---', '-- ', '- .', '- -', '-  ',
    ' ..', ' .-', ' . ', ' -.', ' --', ' - ', '  .', '  -'
    ]

letters = list(string.ascii_uppercase)

def reduce_Keyword(keyword): #Reduces keyword - removes multiple letters
    reduced = ""
    for char in keyword:
        if char.upper() not in reduced:
            reduced+=char.upper()
    return reduced

def createAlphabet(redKeyword): #Creates alphabet using reduced keyword as input
    alphabet = redKeyword
    for char in letters:
        if char not in alphabet:
            alphabet += char
    return alphabet

def doMorse(input, do): #Converts message to morse code
    if do == True:
        morse = ""
        for char in input:
            if char != " ":
                morse+=morse_keys[char.upper()] + " "
            else:
                morse+=" "
        print("Morse: " + morse)
        return morse
    elif do == False:
        #input+=''
        decipher = ''
        citext = ''
        i = 0
        n = 0
        for dat in input:
            n+=1
            if dat != " ":
                i=0
                citext += dat
            else:
                i += 1
                if i == 2:
                    decipher += ' '
                else:
                    decipher += rvmorse_keys[citext]
                    citext = ''
        if citext != '':
            decipher += rvmorse_keys[citext]
            citext=''
        return decipher



def hashKey(alphabet): #makes a dictionary with keys being the keyword alphabet
    new_alphabet = {}
    for i in range(26):
        new_alphabet[fractionated_table[i]] = alphabet[i]
    return new_alphabet

def fractionate(input, keyAlpha, do): #encoding/decoding
    if do == True:
        coded = ''
        if(len(input)%3 != 0):
            for i in range((len(input)%3)):
                input+=" "
        message = re.findall('...', input)
        for i in message:
            coded+=keyAlpha[i]
        return coded
    elif do == False:
        decoded = ''
        switched = {v: k for k, v in keyAlpha.items()}
        for i in input:
            decoded+=switched[i]
        return decoded
def main():
    try:
        repeating = True
        while repeating:
            en_dec = input("Encoding or decoding? (Enter 1 | 2 respectively): ")
            if en_dec == "1":
                keyword = input("\nPlease enter your keyword: ")
                keywordAlphabet = createAlphabet(reduce_Keyword(keyword))
                keyAlphabet = hashKey(keywordAlphabet)
                message = input("Please paste message here: ")
                print("\n" + fractionate(doMorse(message, True), keyAlphabet, True))
            elif en_dec == "2":
                keyword = input("Please enter your keyword: ")
                keywordAlphabet = createAlphabet(reduce_Keyword(keyword))
                keyAlphabet = hashKey(keywordAlphabet)
                message = input("Please enter coded message: ")
                morse = fractionate(message, keyAlphabet, False)
                print("Decoded Message: " + doMorse(morse, False))
            repeat = input("\nWould you like to continue using this program? (y/n): ")
            if(repeat.lower() == "n"):
                repeating = False
                print("Thanks for using this program. See you next time!")
    except KeyboardInterrupt:
        print("\nProgram Exited.")
    except KeyError:
        print("\nWrong key used. Please try again.")
        main()

def frac_console(en_dec, key_input, message_in):
    try:
        if en_dec == "1":
            keywordAlphabet = createAlphabet(reduce_Keyword(key_input))
            keyAlphabet = hashKey(keywordAlphabet)
            message = message_in
            return fractionate(doMorse(message, True), keyAlphabet, True)
        elif en_dec == "2":
            key_input = key_input.upper()
            keywordAlphabet = createAlphabet(reduce_Keyword(key_input))
            keyAlphabet = hashKey(keywordAlphabet)
            morse = fractionate(message_in.upper(), keyAlphabet, False)
            return doMorse(morse, False).lower()
    except KeyError:
        return "Wrong key used. Please try again."

if __name__ == "__main__":
    main()
